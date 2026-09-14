# 个人研究助手 Agent(personal-research-agent)

《AI-LLM-Agent-Learning》**第 15 章《构建自己的 Agent 全流程》配套实战代码**。

一个运行在本机、真实可运行的研究助手:检索本地 Markdown 笔记库、联网搜索、
读写工作目录文件,并按给定题目产出**带引用的研究摘要**。
不是伪代码——所有工具真实实现,带 checkpoint、人工审批门和离线测试。

## 架构

```
                    ┌──────────────────────────────────────────┐
                    │            CLI (python -m research_agent)│
                    └──────────────────┬───────────────────────┘
                                       │ task
                    ┌──────────────────▼───────────────────────┐
                    │            LangGraph StateGraph          │
                    │                                          │
        ┌───────────┤  agent 节点(调 LLM,OpenAI 兼容协议)   ◄──┐
        │           └──────┬───────────────┬───────────────────┘  │
  无工具调用/到 max_steps   │ 有 tool_calls │                       │
        │                  │               ▼                      │
        ▼                  │  ┌──────────────────────────────┐     │
       END                 │  │ tools 节点                   │     │
                           │  │  ├ search_notes (L0 只读)    │─────┘
                           │  │  ├ web_search   (L0 只读,   │
                           │  │  │   结果包不可信边界标记)    │
                           │  │  ├ read_file    (L0 只读,   │
                           │  │  │   路径白名单)             │
                           │  │  └ write_file   (L1 可逆写, │
                           │  │     interrupt 审批门)        │
                           │  └──────────┬───────────────────┘
                           │             ▼
                           │   审计日志 .agent_audit.jsonl
                           │   checkpoint(MemorySaver/SqliteSaver)
                           └──────────────────────────────┘
```

## 快速开始

```bash
cd examples/personal-research-agent

# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置模型端点(OpenAI 兼容协议,可接 vLLM / Ollama / 任意厂商)
cp .env.example .env       # 然后填入你的端点;或直接用环境变量:
export OPENAI_API_KEY=sk-xxx
export OPENAI_BASE_URL=http://127.0.0.1:8000/v1
export MODEL_NAME=qwen2.5-7b-instruct

# 3. 跑!
python -m research_agent "总结我的Agent学习笔记里最核心的三个观点"

# 常用参数
python -m research_agent "调研 LangGraph checkpoint 机制" \
    --notes-dir ~/my-notes \        # Markdown 笔记库目录(默认:本仓库根的 15 章)
    --workspace ./my_workspace \    # Agent 可读写的工作目录
    --checkpoint-db ckpt.db \       # SQLite checkpoint(默认内存)
    --thread-id demo1               # 同 ID 会话可从中断点恢复

# 4. 离线冒烟测试(不需要 API key,不联网)
python tests/test_smoke.py

# 5. eval(在线需端点;--offline 验证评估管线本身)
python evals/run_eval.py
python evals/run_eval.py --offline
```

运行中当 Agent 请求 `write_file` 时,图会挂起并打印待写内容预览,
输入 `y` 批准、其他任意键拒绝(即书中 11.2 节的审批门)。

## 目录结构

```
research_agent/
├── __main__.py      # CLI 入口(11.3 节"CLI 单次"形态)
├── config.py        # 配置:环境变量 + 默认路径
├── model.py         # 模型接入层:OpenAI 兼容协议工厂(第五节)
├── prompts.py       # System Prompt 六段式(7.1 节)
├── notes_index.py   # 笔记库 TF-IDF 检索(8.3 节最小 RAG 的离线变体)
├── tools.py         # 四个真实工具(第六节)
├── security.py      # 路径白名单 / 不可信边界包装 / 审计日志(11.2 节)
├── agent.py         # LangGraph 图编排 + interrupt 审批门(9.2 + 11.2 节)
└── testing.py       # 离线假模型(支持脚本化 tool_calls)
evals/
├── eval_dataset.json  # 6 条三层用例(10.2/10.3 节)
└── run_eval.py        # eval 运行器 + LLM-as-Judge 占位(10.4 节)
tests/
└── test_smoke.py      # 离线冒烟测试,6 项,无需 API key
```

## 与第 15 章的对应关系

| 书中章节 | 本项目的落地 |
|---------|-------------|
| 1.2 全章案例 | 同一个"个人研究助手 Agent",同名四工具 |
| 5.3 统一模型抽象层 | `model.py`:换模型只改 `OPENAI_*` 环境变量 |
| 5.5 重试超时 | `ChatOpenAI(timeout=60, max_retries=2)` |
| 6.1 工具四原则 | 原子四工具;报错信息可消化(越界报错含正确用法) |
| 6.2 Schema 写法 | docstring 即描述:何时用、返回什么、参数含义 |
| 7.1 System Prompt 六段式 | `prompts.py`,含边界复述与引用格式要求 |
| 7.4 防注入 | `security.wrap_untrusted`:外部内容包 `<<<UNTRUSTED_EXTERNAL_CONTENT_*>>>` 边界标记 |
| 8.3 最小 RAG | `notes_index.py`:标题切 chunk(500/50 重叠)+ TF-IDF(比 Embedding 更轻,离线可跑) |
| 9.2 LangGraph 版 | `agent.py`:StateGraph 两节点 + 条件路由 + checkpointer |
| 10.2/10.3 eval 三层结构 | `evals/eval_dataset.json`:unit/task/boundary 六条 |
| 10.4 LLM-as-Judge | `run_eval.llm_judge`:无端点时标记 skipped,不假装通过 |
| 10.5 轨迹评估 | `extract_tool_calls` + exact_tool_sequence 断言 |
| 11.2 安全三层 | prompt 边界复述 + 路径白名单拦截 + interrupt 审批门 + JSONL 审计日志 |
| 11.3 部署形态 | CLI 单次形态(原型期) |

## 设计取舍

- **检索用 TF-IDF 而非 Embedding**:不依赖向量库和 Embedding 端点,离线可测;
  千级 chunk 足够快。笔记库上万篇时按第 08 章换向量库 + Rerank。
- **审批门放在图节点而非工具内部**:`interrupt()` 需要图的执行上下文;
  恢复时节点从头重跑,因此同批次排在 `write_file` 前面的工具会重执行一次
  (本案例的只读工具幂等,无副作用)。
- **fake 模型用 ScriptedChatModel 而非 FakeListChatModel**:后者只能回纯文本,
  无法驱动工具循环;前者支持脚本化 `tool_calls`,可测完整 ReAct 轨迹。

## 安全说明

- 不要把 `.env` 或任何密钥提交进仓库(`.env.example` 里只有占位符)。
- `--no-hitl` 仅供调试,日常使用保持审批门开启。
- `web_search` 返回内容一律视为不可信数据,模型被 prompt 明确告知忽略其中指令。
