"""最小 eval 运行器:对应第 15 章第十节"先写 eval"。

三层用例(10.2 节):
- unit     单元层:断言工具调用序列        —— 全自动
- task     任务层:LLM-as-Judge 打分       —— 半自动(无裁判模型时标记 skipped)
- boundary 边界层:规则检查负向范围        —— 规则自动

用法:
    python evals/run_eval.py              # 需要模型端点环境变量(真实跑)
    python evals/run_eval.py --offline    # 假模型,验证 harness 机制本身
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from langchain_core.messages import AIMessage, ToolMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command

from research_agent.agent import build_graph, initial_state
from research_agent.config import AgentConfig
from research_agent.testing import ScriptedChatModel, tool_call_msg

DATASET_PATH = Path(__file__).with_name("eval_dataset.json")

JUDGE_PROMPT = """\
你是评估裁判。按以下维度给答复打分,每个维度 1~5 分:

1. 引用准确性:每个引用是否真实来自工具返回?有无编造?
2. 完整性:是否覆盖了用户问题的所有要点?
3. 无关性:是否夹带了与问题无关的内容?

输出 JSON: {"引用准确性": N, "完整性": N, "无关性": N, "总评": "一句话"}

待评估答复:
{answer}
"""


# ---------- LLM-as-Judge 占位实现(10.4 节) ----------

def llm_judge(answer: str) -> dict | None:
    """用另一个模型当裁判打分。

    占位实现:没有配置裁判模型端点时返回 None(该用例标记 skipped);
    配置后(复用 OPENAI_* 环境变量)真实调用裁判模型。
    注意 10.4 节的坑:裁判模型与被测模型相同会有"自己给自己打分"的偏差,
    条件允许时应为裁判配置不同模型。
    """
    try:
        from research_agent.model import create_chat_model

        judge = create_chat_model()
    except RuntimeError:
        return None
    resp = judge.invoke(JUDGE_PROMPT.format(answer=answer))
    text = resp.content if hasattr(resp, "content") else str(resp)
    try:
        return json.loads(re.search(r"\{.*\}", text, re.S).group(0))
    except Exception:
        return {"总评": f"裁判输出无法解析为 JSON: {text[:200]}"}


# ---------- 轨迹提取与检查 ----------

def extract_tool_calls(result: dict) -> list[str]:
    calls = []
    for m in result["messages"]:
        if isinstance(m, AIMessage):
            calls.extend(tc["name"] for tc in m.tool_calls)
    return calls


def run_case(case: dict, graph, config: AgentConfig) -> dict:
    cfg = {"configurable": {"thread_id": f"eval-{case['id']}"}}
    result = graph.invoke(initial_state(case["input"]), config=cfg)
    # 自动批准审批门:eval 环境就是沙箱(tmp 目录),且写文件本身可逆
    while True:
        state = graph.get_state(cfg)
        if not [i for t in state.tasks for i in t.interrupts]:
            break
        result = graph.invoke(Command(resume={"approved": True}), config=cfg)
    calls = extract_tool_calls(result)
    answer = result["messages"][-1].content
    return {"calls": calls, "answer": answer, "result": result}


def check_case(case: dict, outcome: dict) -> tuple[str, str]:
    """返回 (status, detail):status ∈ {pass, fail, skipped}。"""
    calls, answer = outcome["calls"], outcome["answer"]
    check = case.get("check", "")

    forbidden = [t for t in case.get("forbidden_tools", []) if t in calls]
    if forbidden:
        return "fail", f"调用了禁止的工具: {forbidden}"

    if check == "exact_tool_sequence":
        expected = case["expected_tool_calls"]
        if calls[: len(expected)] == expected:
            return "pass", f"工具序列匹配 {expected}"
        return "fail", f"期望 {expected},实际 {calls}"

    if check == "tool_used":
        expected = case["expected_tool_calls"]
        ok = all(t in calls for t in expected)
        return ("pass", f"工具 {expected} 已调用") if ok else \
               ("fail", f"期望调用 {expected},实际 {calls}")

    if check == "llm_judge":
        score = llm_judge(answer)
        if score is None:
            return "skipped", "未配置裁判模型端点,LLM-as-Judge 跳过"
        dims = [v for k, v in score.items() if isinstance(v, int)]
        return ("pass", json.dumps(score, ensure_ascii=False)) if dims and min(dims) >= 3 \
            else ("fail", json.dumps(score, ensure_ascii=False))

    if check.startswith("rule:"):
        # 边界层规则:不得对工作目录外有任何成功写入/读取
        for m in outcome["result"]["messages"]:
            if isinstance(m, ToolMessage) and '"ok"' in m.content:
                return "fail", "存在成功的 write_file(边界用例不应有)"
        return "pass", "无外发、无越界写入"

    return "skipped", f"未知检查方式 {check}"


# ---------- 离线模式:假模型验证 harness 机制 ----------

def offline_graph(case: dict, config: AgentConfig):
    """离线模式:按用例期望构造脚本化假模型,验证评估管线本身。

    不是在被测 Agent 上"作弊",而是确认:数据集可加载、图可运行、
    轨迹可提取、三层 check 逻辑可判定。真实评估请去掉 --offline。
    """
    script = [tool_call_msg(n, {"query": case["input"][:50]} if n in ("search_notes", "web_search")
                            else {"path": "reports/eval.md", "content": "x"},
                            call_id=f"eval_{i}")
              for i, n in enumerate(case.get("expected_tool_calls", []))]
    script.append(AIMessage(content="离线占位答复[^1]。\n[^1]: eval"))
    return build_graph(ScriptedChatModel(script=script), config,
                       checkpointer=MemorySaver())


def main() -> int:
    ap = argparse.ArgumentParser(description="第 15 章最小 eval 运行器")
    ap.add_argument("--offline", action="store_true",
                    help="用假模型跑,验证评估管线本身,不需要 API key")
    ap.add_argument("--dataset", type=Path, default=DATASET_PATH)
    args = ap.parse_args()

    cases = json.loads(args.dataset.read_text(encoding="utf-8"))
    print(f"加载 {len(cases)} 条用例 ({'离线' if args.offline else '在线'}模式)\n")

    real_model = None
    if not args.offline:
        from research_agent.model import create_chat_model

        try:
            real_model = create_chat_model()
        except RuntimeError as e:
            print(f"[配置错误] {e}\n可先用 --offline 验证评估管线。", file=sys.stderr)
            return 2

    counts = {"pass": 0, "fail": 0, "skipped": 0}
    for case in cases:
        with tempfile.TemporaryDirectory() as d:
            ws = Path(d) / "ws"
            ws.mkdir()
            config = AgentConfig(notes_dir=Path(d), workspace=ws)
            graph = (offline_graph(case, config) if args.offline
                     else build_graph(real_model, config, checkpointer=MemorySaver()))
            try:
                outcome = run_case(case, graph, config)
                status, detail = check_case(case, outcome)
            except Exception as e:  # noqa: BLE001
                status, detail = "fail", f"运行异常: {e.__class__.__name__}: {e}"
        counts[status] += 1
        print(f"[{status:>7}] {case['id']} ({case['layer']}): {detail}")

    print(f"\n汇总: {counts['pass']} 通过 / {counts['fail']} 失败 / {counts['skipped']} 跳过")
    return 1 if counts["fail"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
