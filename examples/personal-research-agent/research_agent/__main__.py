"""CLI 入口:python -m research_agent "研究题目"

对应第 15 章 11.3 节"CLI 单次"部署形态(原型期)。

示例:
    python -m research_agent "总结我的笔记里最核心的三个观点"
    python -m research_agent "调研 LangGraph 的 checkpoint 机制" \
        --notes-dir ~/notes --workspace ./ws --no-hitl --thread-id demo1
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from langgraph.types import Command

from .agent import build_graph, initial_state
from .config import AgentConfig


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="python -m research_agent",
        description="个人研究助手 Agent(第 15 章配套实战代码)",
    )
    p.add_argument("query", help="研究题目 / 任务描述")
    p.add_argument("--notes-dir", type=Path, default=None,
                   help="Markdown 笔记库目录(默认:本仓库根目录的章节文件)")
    p.add_argument("--workspace", type=Path, default=None,
                   help="Agent 读写的工作目录(默认:examples/personal-research-agent/agent_workspace)")
    p.add_argument("--no-hitl", action="store_true",
                   help="关闭 write_file 的人工审批门(不推荐,仅调试用)")
    p.add_argument("--checkpoint-db", type=Path, default=None,
                   help="SQLite checkpoint 文件路径;不传则用内存 checkpoint")
    p.add_argument("--thread-id", default="default",
                   help="会话线程 ID,同 ID 可从中断点恢复")
    p.add_argument("--max-steps", type=int, default=25, help="最大循环步数(防空转)")
    return p.parse_args(argv)


def _make_checkpointer(db_path: Path | None):
    if db_path is None:
        return None  # build_graph 内部默认 MemorySaver
    from langgraph.checkpoint.sqlite import SqliteSaver

    return SqliteSaver.from_conn_string(str(db_path))


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    config = AgentConfig(
        notes_dir=args.notes_dir or AgentConfig.__dataclass_fields__["notes_dir"].default,
        workspace=args.workspace or AgentConfig.__dataclass_fields__["workspace"].default,
        hitl=not args.no_hitl,
        max_steps=args.max_steps,
    )

    # 模型接入:OpenAI 兼容协议(环境变量驱动,见 config.py)
    from .model import create_chat_model

    try:
        model = create_chat_model()
    except RuntimeError as e:
        print(f"[配置错误] {e}", file=sys.stderr)
        return 2

    checkpointer = _make_checkpointer(args.checkpoint_db)
    graph = build_graph(model, config, checkpointer=checkpointer)
    run_config = {"configurable": {"thread_id": args.thread_id}}

    result = graph.invoke(initial_state(args.query), config=run_config)

    # HITL 审批门:图在 write_file 前挂起,这里循环询问人类
    while True:
        state = graph.get_state(run_config)
        pending = [i for t in state.tasks for i in t.interrupts]
        if not pending:
            break
        hit = pending[0].value
        print("\n[审批门] Agent 请求写入文件:")
        print(f"  路径: {hit['args'].get('path')}")
        print(f"  内容预览: {str(hit['args'].get('content'))[:300]}")
        ans = input("  批准写入? [y/N] ").strip().lower()
        result = graph.invoke(
            Command(resume={"approved": ans in ("y", "yes")}), config=run_config
        )

    final = result["messages"][-1]
    print("\n===== 研究摘要 =====\n")
    print(final.content if hasattr(final, "content") else final)
    print(f"\n(步数: {result['step_count']}, 审计日志: {config.audit_log})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
