# AI / LLM / Agent 全栈深度学习资源索引

> 按 11 大类系统组织 AI 全栈知识:**交互入口 → 通信协议 → 智能体主体 → 能力约束 → 任务编排 → 提示推理 → 记忆状态 → RAG 知识库 → 模型底座 → 部署运维 → 安全评估**,另加三篇专题:**《12-主流Agent对比分析》**(市场选型)、**《13-自托管个人Agent》**(OpenClaw/Hermes 框架解读)、**《14-多模态Agent》**(VLM/GUI 操作/语音原理笔记)。所有内容已对照 2026 年最新官方文档与社区实践整理。本 README 是整个知识体系的"地图 + 索引 + 学习指南",看完它你就能找到任何 AI 工程化概念的位置。

---

## ⚠️ 重要声明(必读)

> **这是一份个人学习笔记,绝非权威资料。**

- 📝 **性质说明:** 本仓库是作者在学习 AI / LLM / Agent 过程中整理的**个人学习笔记**,内容来源于官方文档、开源社区、论文、博客以及自己的理解与总结,仅作为学习交流之用。
- 🙏 **能力有限:** 作者水平有限,接触 AI 时间不长,文中很多理解可能**片面、浅显、甚至存在错误**。对于复杂技术概念的解读难免有失偏颇,敬请批评指正。
- ⚠️ **不保证准确:** 文档中部分内容可能**过时、不准确或不完整**,AI 领域发展极快,请以官方文档和最新论文为准。读者请**独立判断**,不要将此处内容作为生产决策的唯一依据。
- 🔗 **来源声明:** 文中引用了大量官方文档、论文、开源项目链接,版权归原作者所有。如有遗漏署名或侵权,请联系作者删除。
- 💬 **欢迎指正:** 任何错误、建议、补充都欢迎通过 Issue 或 PR 提出,作者会虚心接受并改进。本文档内所有相关论文存在ai伪造可能，请不要相信，大部分官网链接大部分可直达相关的学习途径，虚心求教中。
- 🚫 **非商业用途:** 本仓库内容仅供学习交流,**禁止用于商业用途**。

> **"知之为知之,不知为不知,是知也。"** —— 《论语》
> 作者仍在持续学习中,这份笔记会不断修正和完善,也希望能与同行一起进步。

---

## 📑 目录

- [📁 一、文档结构总览(11 大类 + 3 专题 + README)](#一文档结构总览11-大类--3-专题--readme)
- [🗺️ 二、知识体系架构图](#二知识体系架构图)
- [📖 三、11 大类 + 3 专题一句话定位与深度内容](#三11-大类--3-专题一句话定位与深度内容)
- [🚀 四、推荐学习路径(4 种顺序)](#四推荐学习路径4-种顺序)
- [📚 五、全局专业词汇索引(A-Z)](#五全局专业词汇索引a-z)
- [🏷️ 六、技术栈全景图](#六技术栈全景图)
- [🎯 七、应用场景对照表](#七应用场景对照表)
- [🛠️ 八、推荐工具清单(按场景)](#八推荐工具清单按场景)
- [📄 九、经典必读论文 / 文章 / 白皮书](#九经典必读论文--文章--白皮书)
- [🔗 十、快速入口(官方文档)](#十快速入口官方文档)
- [❓ 十一、常见问题 FAQ](#十一常见问题-faq)
- [💡 十二、学习心法与方法论](#十二学习心法与方法论)
- [⚠️ 十三、学习前置要求](#十三学习前置要求)
- [📅 十四、技术版本基准(2026-07)](#十四技术版本基准2026-07)
- [📊 十五、文档统计与版本日志](#十五文档统计与版本日志)

---

## 一、文档结构总览(11 大类 + 3 专题 + README)

| 序号 | 文档 | 内容定位 | 关键词 | 优先级 | 行数 |
|------|------|----------|--------|--------|------|
| 00 | `README.md` | 本文件 - 总览索引与学习路径 | 索引/路径/词汇 | 必读 | 本文件 |
| 01 | `01-交互入口.md` | CLI / WebUI / Widget / Copilot / Chatbot / ASR / TTS / Realtime | 7 大入口 | 基础 | ~1230 |
| 02 | `02-智能体通信协议.md` | MCP / A2A / Registry / 消息队列 / Handoff 任务移交 | MCP/A2A | 核心 | ~1940 |
| 03 | `03-智能体主体.md` | Agent / Multi-Agent / Sub-agent / ADK / 框架对比 | Agent 形态 | 核心 | ~1370 |
| 04 | `04-能力与约束体系.md` | skill / CLAUDE.md / Rules / Hooks / 工具调用 / 沙箱 | 能力/约束 | 核心 | ~1230 |
| 05 | `05-任务流程编排.md` | Workflow / Orchestrator / Plan / Durable Execution / HITL | 编排/调度 | 核心 | ~2120 |
| 06 | `06-提示与推理逻辑.md` | Prompt / CoT / Structured Output / 推理模型 / 提示评估 | 提示/推理 | 基础 | ~1820 |
| 07 | `07-记忆会话状态.md` | Memory / Session / State / Mem0 / LangGraph Store | 记忆/状态 | 基础 | ~1720 |
| 08 | `08-RAG知识库体系.md` | RAG / GraphRAG / LightRAG / VectorDB / 混合检索 | 检索增强 | 重要 | ~2430 |
| 09 | `09-底层大模型底座.md` | LLM / MoE / LoRA / GRPO / 推理模型 / 量化 | 模型基础 | 重要 | ~1860 |
| 10 | `10-部署网关运维.md` | vLLM / P/D 分离 / Ollama / OneAPI / 监控 / 故障 Runbook | 工程化 | 实战 | ~2980 |
| 11 | `11-安全对齐评估.md` | Evaluation / GRPO / RLVR / Alignment / Guardrails | 安全/评估 | 进阶 | ~2460 |
| 12 | `12-主流Agent对比分析.md` | Claude Code / Codex / Cursor / Devin / 框架与平台选型 | 专题·选型 | 实战 | ~1020 |
| 13 | `13-自托管个人Agent.md` | OpenClaw(小龙虾)/ Hermes Agent(爱马仕)/ 自托管架构与安全 | 专题·自托管 | 实战 | ~810 |
| 14 | `14-多模态Agent.md` | VLM / GUI 操作 / Computer Use / 语音端到端 / 多模态安全 | 专题·多模态 | 基础 | ~1010 |
| 15 | `15-构建自己的Agent全流程.md` | 九阶段生命周期 / 框架选型 / 架构设计 / 手写 vs LangGraph 双版本实战 / 安全部署 | 专题·实战 | 实战 | ~1138 |

> 全套合计 **~25,700 行** Markdown,涵盖 **500+ 速查术语**、**550+ 表格/图示**、**600+ 代码/命令/配置示例块**。

---

## 二、知识体系架构图

```
┌────────────────────────────────────────────────────────────────────────────┐
│                                                                            │
│              🌐 AI 全栈知识体系(11 大类 + 总览)                            │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  [应用层] 用户接触面与生产化                                          │  │
│  │                                                                       │  │
│  │   01 交互入口 ──► 10 部署运维 ──► 11 安全评估                          │  │
│  │   (CLI/WebUI/    (vLLM/网关/    (评估/对齐/                            │  │
│  │    语音/Copilot)  K8s/监控)       护栏/合规)                           │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                  ▲                                         │
│                                  │ 服务化                                  │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  [核心层] Agent 主体与协作                                            │  │
│  │                                                                       │  │
│  │   03 智能体主体 ◄── 02 通信协议 ──► 04 能力约束 ──► 05 任务编排        │  │
│  │   (Agent/         (MCP/A2A/     (Skills/Hooks/   (Workflow/          │  │
│  │    Multi-Agent/    Handoff)      CLAUDE.md)       Orchestrator)      │  │
│  │    Sub-agent)                                                         │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                  ▲                                         │
│                                  │ 调用                                    │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  [认知层] 推理 / 记忆 / 知识                                          │  │
│  │                                                                       │  │
│  │   06 提示推理 ──► 07 记忆状态 ──► 08 RAG 知识库                        │  │
│  │   (Prompt/CoT/   (Memory/Session/   (RAG/GraphRAG/                    │  │
│  │    Reflection)    VectorDB)          VectorDB)                        │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                  ▲                                         │
│                                  │ 基础                                    │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  [基础层] 模型底座                                                    │  │
│  │                                                                       │  │
│  │   09 底层大模型底座                                                    │  │
│  │   (LLM/Transformer/Attention/MoE/LoRA/                                │  │
│  │    RLHF/Tokenizer/量化/KV Cache)                                       │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

**四层结构逻辑:**

| 层次 | 章节 | 职责 | 关键问题 |
|------|------|------|---------|
| **基础层** | 09 | LLM 的原理与技术栈 | "AI 是什么?" |
| **认知层** | 06 / 07 / 08 | 提示/记忆/知识 | "AI 如何思考和记忆?" |
| **核心层** | 02 / 03 / 04 / 05 | Agent 主体与协作 | "AI 如何自主行动?" |
| **应用层** | 01 / 10 / 11 | 用户接入与生产化 | "AI 如何服务和被信任?" |

> 📌 **专题篇:** `12-主流Agent对比分析.md`、`13-自托管个人Agent.md`、`14-多模态Agent.md`、`15-构建自己的Agent全流程.md` 不属于四层结构——前三篇是原理知识的"市场落点"与方向深化,第四篇是从零构建 Agent 的完整工程方法论(九阶段生命周期 / 框架选型 / 双版本实战 / 安全部署),回答"学完原理后该买/用/装哪个"、"Agent 如何长出眼睛和耳朵"以及"我要自己造一个 Agent 该怎么动手"。

---

## 三、11 大类 + 3 专题一句话定位与深度内容

> 每章开头都有术语速查表(21~50 条,中英文对照 + 一句话解释),正文中所有专业词汇均有解释。

### 1. **交互入口(01)** — 用户与 AI 系统的接触面

- **一句话:** 从 CLI 到语音交互的 7 种入口形态。
- **核心概念:** CLI、WebUI、Widget、Copilot、Chatbot、ASR、TTS
- **代表工具:** Codex CLI、Claude Code、Cursor、ChatGPT、Whisper
- **关键问题:** 用户如何"使用" AI?

### 2. **智能体通信协议(02)** — Agent 接入外部世界的标准协议

- **一句话:** MCP(Agent↔工具)+ A2A(Agent↔Agent)。
- **核心概念:** MCP、A2A、Function Calling、JSON-RPC 2.0、Streamable HTTP、Agent Card、Handoff
- **关键创新:** M×N 集成降为 M+N(2024-11 Anthropic 开源)
- **关键问题:** Agent 之间和 Agent 与工具如何"对话"?

### 3. **智能体主体(03)** — Agent 本身的形态与角色

- **一句话:** Agent 形态、角色、多 Agent 协作与主流框架。
- **核心概念:** Agent、Agent Loop、ReAct、Multi-Agent、Sub-agent、Coordinator、Supervisor、Orchestrator
- **主流框架:** LangGraph、CrewAI、OpenAI Agents SDK、AutoGen、DSPy、LlamaIndex
- **关键问题:** Agent 是什么?如何"自主行动"?

### 4. **能力与约束体系(04)** — Agent 的能力扩展与行为边界

- **一句话:** 能力封装(skill/tool)+ 行为约束(CLAUDE.md/Rules/Hooks)。
- **核心概念:** Skill、CLAUDE.md、AGENTS.md、Rules、Hooks、PreToolUse、PostToolUse、Sandbox
- **关键标准:** AGENTS.md(60k+ 项目采用)、AgentSkills.io
- **关键问题:** Agent "能做什么"和"不能做什么"?

### 5. **任务流程编排(05)** — 任务拆解、调度、闭环

- **一句话:** Anthropic 五大工作流 + Plan/ReAct/Reflection 三大范式。
- **核心概念:** Workflow、Prompt Chaining、Routing、Evaluator-Optimizer、Orchestrator-Workers、DAG、Feedback Loop、Trigger、Webhook、Cron
- **关键论文:** Anthropic《Building Effective Agents》(2024-12)
- **关键问题:** 任务从输入到输出"怎么跑"?

### 6. **提示与推理逻辑(06)** — 控制模型输出的核心机制

- **一句话:** Prompt 工程 + CoT/ReAct/Reflection/ToT/GoT 推理模式。
- **核心概念:** Prompt、System Prompt、Zero-shot、Few-shot、CoT、ToT、GoT、Self-Consistency、Reflection、Grounding、DSPy
- **关键参数:** Temperature、Top-p、Top-k、Max Tokens、Stop Sequence
- **关键问题:** 如何精确"指挥" LLM?

### 7. **记忆会话状态(07)** — Agent 的上下文与状态管理

- **一句话:** 三层记忆(工作/短期/长期)+ 会话状态机。
- **核心概念:** Memory、Working/Short-term/Long-term Memory、Session、State Machine、Scratchpad、Vector Database、MemGPT、Generative Agents、Reflexion
- **关键论文:** MemGPT(OS 思想管理上下文)、Generative Agents(斯坦福小镇)
- **关键问题:** Agent 如何"记住"和"思考"?

### 8. **RAG 知识库体系(08)** — 检索增强生成技术栈

- **一句话:** 从朴素 RAG 到 GraphRAG/RAPTOR/Self-RAG/CRAG 的演进。
- **核心概念:** RAG、Naive/Advanced/Modular RAG、GraphRAG、RAPTOR、HippoRAG、Self-RAG、CRAG、Embedding、Chunk、HNSW、IVF、PQ、Hybrid Search、Reranker、HyDE、RAGAS
- **主流向量库:** Milvus、Qdrant、Weaviate、Chroma、Pinecone、PGVector
- **关键问题:** Agent 如何"开卷考试"、接入外部知识?

### 9. **底层大模型底座(09)** — LLM 的原理与技术栈

- **一句话:** Transformer/Attention/MoE/LoRA/RLHF/量化全栈。
- **核心概念:** LLM、VLM、MMM、Transformer、Attention、MHA/MQA/MLA/GQA、MoE、Tokenizer、BPE、Embedding、Pre-training、SFT、RLHF、PPO、DPO、KTO、ORPO、RLAIF、Constitutional AI、LoRA、QLoRA、DoRA、PEFT、GPTQ、AWQ、GGUF、KV Cache、FlashAttention、Speculative Decoding、RoPE、ALiBi
- **主流模型:** GPT-4o/5、Claude 4、Gemini 2.5、Llama 4、DeepSeek-V3/R1、Qwen 3、Mistral、GLM-4.5、Grok
- **关键问题:** AI 上层所有能力的"源头"是什么?

### 10. **部署网关运维(10)** — 模型部署、网关、监控、运维

- **一句话:** AI 工程化的"最后一公里"。
- **核心概念:** vLLM、PagedAttention、Continuous Batching、TGI、Ollama、TensorRT-LLM、SGLang、llama.cpp、GGUF、TP/PP/EP/CP/DP、KV Cache、Prefix Cache、Prompt Caching、Semantic Cache、OneAPI、LiteLLM、Higress、Token Bucket、Leaky Bucket、OAuth 2.1、PKCE、JWT、TTFT、TPOT、QPS、Prometheus、Grafana、LangSmith、Langfuse、Docker、K8s、HPA、KEDA、KubeAI、KServe
- **关键问题:** 如何把模型变成可用的生产服务?

### 11. **安全对齐评估(11)** — 模型评估、安全护栏、对齐与合规

- **一句话:** AI 工程化的"守门员"。
- **核心概念:** Evaluation、Benchmark、MMLU、MMLU-Pro、GSM8K、MATH、GPQA、HumanEval、MBPP、SWE-bench、AgentBench、τ-bench、GAIA、LiveBench、LMSYS Arena、Pass@k、Elo Rating、LLM-as-a-Judge、Hallucination、FActScore、TruthfulQA、Alignment、HHH、Constitutional AI、Scalable Oversight、RLHF、RLAIF、Alignment Tax、Guardrails、NeMo Guardrails、Llama Guard、Moderation、OpenAI Moderation API、Perspective API、Prompt Injection、Jailbreak、DAN、Many-shot Jailbreak、OWASP LLM Top 10、PII、Differential Privacy、Federated Learning、Bias、Fairness、Toxicity、Audit、Compliance、Interpretability、Mechanistic Interpretability、Red Team、EU AI Act、生成式 AI 管理办法、NIST AI RMF、ISO 42001
- **关键问题:** 如何让 AI 安全可控地服务人类?

### 12. **主流 Agent 对比分析(12 · 专题篇)** — 2026 年市场格局与选型决策

- **一句话:** 前面 11 章讲"Agent 怎么造",本章讲"Agent 怎么选"。
- **核心内容:** 编程 Agent 产品(Claude Code / Codex / Cursor / Copilot / Devin / Jules / Gemini CLI / 开源阵营)、通用 Agent(ChatGPT Agent / Manus / Kimi)、开发框架(LangGraph / CrewAI / OpenAI Agents SDK / Claude Agent SDK / Google ADK / MS Agent Framework / Pydantic AI / LlamaIndex)、企业托管平台(AgentKit / Bedrock AgentCore / Vertex AI / Copilot Studio 等)
- **特色:** 三张自绘对比图(定位图 / 基准对比 / 框架雷达)+ 四层市场全景 + 决策树 + 场景推荐表
- **关键问题:** 2026 年我该买/用哪个 Agent?

### 13. **自托管个人 Agent(13 · 专题篇)** — OpenClaw(小龙虾)与 Hermes Agent(爱马仕)框架解读

- **一句话:** 2026 年最火的开源品类——跑在自己机器上、聊天软件指挥、7×24 待命的私人 AI 管家。
- **核心内容:** 小龙虾/爱马仕花名与社区黑话、共同范式(常驻进程+Gateway+全系统工具面)、Hermes 学习循环架构、OpenClaw 白盒可控哲学、部署上手与成本、Shell 级权限的安全风险
- **特色:** 两张自绘对比图(能力雷达 / 社区热度)+ 消息全生命周期时序图 + 攻击链分析
- **关键问题:** 要不要"养虾/养马"?养哪只?怎么养才安全?

### 14. **多模态 Agent(14 · 专题篇)** — VLM 原理、GUI 操作与端到端语音

- **一句话:** Agent 如何长出"眼睛"和"耳朵"——感知图像/语音/屏幕并采取行动的笔记。
- **核心概念:** VLM、CLIP/SigLIP、Visual Grounding、Computer Use、GUI Agent、ASR/TTS、端到端语音、全双工、多模态 RAG、OSWorld、视觉提示注入
- **特色:** LLaVA 架构图、看屏决策循环、语音延迟预算、Playwright/faster-whisper/FastMCP 可运行示例(纯笔记体,不含费用分析)
- **关键问题:** 模型怎么"看懂"图、"听懂"话、替你操作屏幕?

### 15. **构建自己的Agent全流程(15 · 专题篇)** — 从需求定义到部署上线的完整工程方法论

- **一句话:** 手把手教你如何从零构建一个生产级 Agent——不是学"Agent 是什么",而是学"Agent 怎么做"。
- **核心概念:** 九阶段生命周期、框架分析六维模型、单/多Agent架构设计、模型接入层、工具设计与MCP封装、提示词工程、记忆与RAG接入、手写vs LangGraph双版本实战、评估与迭代闭环、安全加固与部署上线、十大失败模式
- **特色:** 框架决策树与六维雷达、手写 Agent Loop vs LangGraph 双版本完整可运行代码对比、MCP 工具封装实战、十大失败模式排查表
- **关键问题:** 我要自己造一个 Agent,从哪开始、用什么框架、怎么上线?

---

## 四、推荐学习路径(4 种顺序)

### 🚀 路径 A:递进式(适合初学者,从底层到应用)

```
第 1 步: 09 底层模型 ────► 了解 LLM 是什么
                              ↓
第 2 步: 06 提示推理 ────► 学会用 Prompt 控制输出
                              ↓
第 3 步: 07 记忆状态 ────► 理解上下文/记忆/状态
                              ↓
第 4 步: 03 智能体主体 ──► Agent 三要素与循环
                              ↓
第 5 步: 04 能力约束 ────► 工具/Skills/Hooks/CLAUDE.md
                              ↓
第 6 步: 05 任务编排 ────► 五大工作流模式
                              ↓
第 7 步: 02 通信协议 ────► MCP 协议原理与实践
                              ↓
第 8 步: 01 交互入口 ────► CLI 工具实操
                              ↓
第 9 步: 08 RAG 体系 ────► 向量数据库/RAG/GraphRAG
                              ↓
第 10 步: 10 部署运维 ───► vLLM/Ollama/OneAPI/监控
                              ↓
第 11 步: 11 安全评估 ───► 对齐/护栏/评估/合规
```

### ⚡ 路径 B:实战优先(适合工程师,先跑起来再深入)

```
第 1 步: 01 交互入口 ────► Codex CLI / Claude Code 跑起来
第 2 步: 09 底层模型 ────► 选个 LLM 用(API/本地)
第 3 步: 10 部署运维 ────► vLLM/Ollama 部署
第 4 步: 02 通信协议 ────► 写第一个 MCP Server
第 5 步: 06 提示推理 ────► 优化 Prompt
第 6 步: 03 智能体主体 ──► 写第一个 Agent
第 7 步: 04 能力约束 ────► 加 Skills + Hooks
第 8 步: 05 任务编排 ────► 多步任务编排
第 9 步: 07 记忆状态 ────► 加记忆与会话
第 10 步: 08 RAG 体系 ───► 接入知识库
第 11 步: 11 安全评估 ───► 上线前安全检查
```

### 🎯 路径 C:研究优先(适合研究者,从原理到系统)

```
第 1 步: 09 底层模型 ────► Transformer/Attention/MoE 原理
第 2 步: 06 提示推理 ────► CoT/ToT/GoT/Self-Consistency 论文
第 3 步: 11 安全评估 ────► RLHF/DPO/Constitutional AI/Hallucination
第 4 步: 07 记忆状态 ────► MemGPT/Generative Agents 论文
第 5 步: 08 RAG 体系 ────► GraphRAG/RAPTOR/Self-RAG/CRAG 论文
第 6 步: 03 智能体主体 ──► ReAct/Reflexion 论文 + 框架对比
第 7 步: 05 任务编排 ────► Anthropic 五大工作流 + LLMCompiler
第 8 步: 02 通信协议 ────► MCP/A2A 规范
第 9 步: 04 能力约束 ────► AGENTS.md / CLAUDE.md 标准
第 10 步: 01 交互入口 ───► CLI/WebUI 形态对比
第 11 步: 10 部署运维 ───► vLLM/PagedAttention 论文 + K8s 实践
```

### 🛠️ 路径 D:按角色(适合不同岗位快速定位)

| 角色 | 推荐顺序 | 重点章节 |
|------|---------|---------|
| **后端工程师** | 10 → 02 → 09 → 08 → 11 | 部署运维 + 协议 + 模型底座 + RAG + 安全 |
| **前端工程师** | 01 → 06 → 03 → 04 | 交互入口 + 提示 + Agent 主体 + 能力约束 |
| **算法工程师** | 09 → 06 → 11 → 08 → 07 | 模型 + 提示 + 评估 + RAG + 记忆 |
| **DevOps** | 10 → 02 → 11 → 01 | 部署 + 协议 + 安全 + 入口 |
| **产品经理** | 01 → 03 → 05 → 06 → 11 | 入口 + Agent + 编排 + 提示 + 安全 |
| **研究者** | 09 → 06 → 07 → 08 → 11 → 03 | 模型 + 提示 + 记忆 + RAG + 评估 + Agent |
| **学生入门** | 09 → 06 → 03 → 01 → 02 | 模型 + 提示 + Agent + 入口 + 协议 |

---

## 五、全局专业词汇索引(A-Z)

> 汇总 11 章中的核心术语,标注所在章节。每个术语在对应章节都有详细解释。

### A

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| A2A | Agent 间协议 | 02 | Google 2025-04 发布的 Agent↔Agent 协议 |
| AdaLoRA | 自适应 LoRA | 09 | 自适应分配秩的 LoRA |
| Advanced RAG | 高级 RAG | 08 | 增加预检索/后检索优化的 RAG |
| Agent | 智能体 | 03 | LLM 为大脑,能自主循环调用工具的系统 |
| Agent Card | Agent 名片 | 02 | A2A 中描述能力的 JSON-LD 名片 |
| Agent Loop | 智能体循环 | 03 | LLM 思考→调用工具→观察→判断完成的 while 循环 |
| AgentBench | AgentBench | 11 | 多环境 Agent 能力评估基准 |
| AGENTS.md | 跨工具规则标准 | 04 | 60k+ 项目采用的跨 CLI Agent 配置标准 |
| AgentSkills.io | 技能标准 | 04 | Skill 的开放标准与目录网站 |
| Agentic | 智能体化 | 01 | 具备自主决策、工具调用能力的特性 |
| Agentic AI | 智能体 AI | 03 | 强调 AI 系统的自主行动能力 |
| Alignment | 对齐 | 11 | 让 AI 行为与人类意图/价值观一致 |
| Alignment Tax | 对齐税 | 11 | 为安全牺牲部分能力 |
| ALiBi | ALiBi 位置编码 | 09 | Attention with Linear Biases 位置编码 |
| Allowlist | 白名单 | 04 | 显式允许的列表 |
| ANN | 近似最近邻 | 08 | Approximate Nearest Neighbor 搜索 |
| API Key | 接口密钥 | 10 | 字符串形式的密钥 |
| API Tool | API 工具 | 04 | 封装 HTTP API 为可被 LLM 调用的工具 |
| Artifact | 产物 | 02 | A2A 中任务产生的最终输出 |
| ASR | 自动语音识别 | 01 | 将语音转换为文字 |
| Audit | 审计 | 11 | 记录和审查系统操作 |
| Auth | 鉴权 | 10 | 身份验证与授权 |
| Auto Memory | 自动记忆 | 07 | Claude Code 自动写入/读取的持久化记忆 |

### B

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| BPE | 字节对编码 | 09 | Byte Pair Encoding,最常用的分词算法 |
| BBH | Big-Bench Hard | 11 | BIG-Bench 中最难的 23 个任务 |
| Bearer Token | 持有者令牌 | 02 | HTTP Authorization 头中携带的访问令牌 |
| Bias | 偏见 | 11 | 模型输出的系统性偏差 |
| Bloom Filter | 布隆过滤器 | 07 | 概率型数据结构,用于快速判重 |

### C

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| Capability Negotiation | 能力协商 | 02 | 握手阶段双方声明支持哪些原语 |
| Chain | 推理执行链 | 05 | 多步串行调用(LangChain 概念) |
| Chatbot | 对话机器人 | 01 | 以对话为核心的 AI 应用 |
| Checkpoint | 检查点 | 07/09 | 训练中保存的模型权重 / 中间状态 |
| Checkpointer | 检查点机制 | 03/07 | LangGraph 中保存中间状态 |
| Chunk | 文本块 | 08 | 文档切分后的最小检索单元 |
| Chunking | 分块 | 08 | 把长文档切分为块的过程 |
| Cipher Jailbreak | 加密越狱 | 11 | 用编码/加密绕过安全 |
| CLI | 命令行接口 | 01 | 通过文本命令与系统交互的终端界面 |
| CLAUDE.md | Claude 项目规则 | 04 | Claude Code 启动时自动加载的项目规则 |
| Code Interpreter | 代码解释器 | 04 | 沙箱中执行代码的工具 |
| Cold Start | 冷启动 | 10 | 模型加载过程,延迟高 |
| Compliance | 合规 | 11 | 符合法规和标准 |
| Continuous Batching | 连续批处理 | 10 | 动态加入/移除请求的批处理方式 |
| Context Window | 上下文窗口 | 06/09 | 模型一次能处理的最大 Token 数 |
| Conversation History | 对话历史 | 07 | 会话中的完整消息序列 |
| CoT | 思维链 | 06 | Chain of Thought,显式推理步骤 |
| Coordinator | 协调智能体 | 03 | 负责任务分配与汇总的调度中心 |
| Copilot | 副驾驶 | 01 | IDE 内辅助编码的 AI 工具 |
| CRAG | 纠正 RAG | 08 | Corrective RAG,检索结果评估与纠正 |
| Crew | 团队 | 03 | CrewAI 中一组 Agent 协作的集合 |
| Cron | 定时任务 | 05 | Unix 系统的定时任务表达式 |

### D

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| DAN | DAN 越狱 | 11 | Do Anything Now,经典越狱 |
| DAG | 有向无环图 | 05 | Directed Acyclic Graph,任务依赖表示 |
| Data Contamination | 数据污染 | 11 | 评估数据混入训练数据 |
| Decode | 解码 | 10 | 自回归逐 Token 生成阶段 |
| Demographic Parity | 人口统计平等 | 11 | 公平性指标 |
| Denylist | 黑名单 | 04 | 显式禁止的列表 |
| Dependency | 任务依赖 | 05 | 任务间的前置关系 |
| Deterministic | 确定性 | 04 | 相同输入永远产生相同输出 |
| Differential Privacy | 差分隐私 | 11 | DP,数学可证明的隐私保护 |
| Distillation | 模型蒸馏 | 09 | 大模型(教师)教小模型(学生) |
| DoRA | 权重分解 LoRA | 09 | Decomposed LoRA |
| DPO | 直接偏好优化 | 09 | Direct Preference Optimization |
| DP | 数据并行 | 10 | Data Parallelism,多副本并行处理 |
| DSPy | DSPy 框架 | 06 | Stanford 的提示编程框架 |

### E

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| Embedding | 嵌入向量 | 08/09 | 把文本/图像映射为高维向量 |
| Elo Rating | Elo 评分 | 11 | 国际象棋式评分,用于模型排名 |
| Embedding Model | 嵌入模型 | 08 | 文本转向量的模型 |
| EP | 专家并行 | 10 | Expert Parallelism,MoE 专家分到多 GPU |
| Episodic Memory | 情节记忆 | 07 | 记录具体事件和经历的记忆 |
| Equal Opportunity | 机会平等 | 11 | 公平性指标 |
| EU AI Act | 欧盟 AI 法案 | 11 | 全球首个综合 AI 监管法 |
| Evaluator-Optimizer | 评估-优化 | 05 | LLM 生成,另一 LLM 评估,迭代改进 |
| Evaluation | 评估 | 11 | 对模型能力/安全性/质量进行量化测量 |
| Elicitation | 信息征询 | 02 | Server 向用户请求额外信息(2025-06) |

### F

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| FActScore | FActScore | 11 | 细粒度事实准确性评估 |
| Fairness | 公平性 | 11 | 不同群体获得公平对待 |
| Federated Learning | 联邦学习 | 11 | 数据不出本地,只传模型更新 |
| Feedback Loop | 反馈闭环 | 05 | 输出反馈到输入的循环优化 |
| FIFO | 先进先出 | 05 | 最简单的调度策略 |
| Few-shot | 少样本 | 06 | 提示中给出几个示例引导模型 |
| Few-shot CoT | 少样本思维链 | 06 | 给出带推理步骤的示例 |
| FlashAttention | Flash Attention | 09 | GPU 友好的 Attention 优化 |
| FP16/BF16/FP8 | 数值精度 | 09 | 16/16/8 位浮点精度 |
| Function Calling | 函数调用 | 02/04 | OpenAI 的工具调用接口规范 |

### G

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| GAIA | GAIA | 11 | 真实世界助理任务评估 |
| Generative Agents | 生成式智能体 | 07 | 斯坦福小镇论文,模拟人类记忆 |
| GGUF | GGUF 格式 | 09/10 | llama.cpp 的量化模型格式 |
| GoT | 思维图 | 06 | Graph of Thoughts,图状推理网络 |
| GPQA | GPQA | 11 | 研究生科学题基准 |
| GPTQ | GPTQ 量化 | 09 | 基于二阶信息的量化 |
| Grafana | Grafana | 10 | 可视化仪表盘 |
| Grounding | 事实锚定 | 06 | 用外部事实约束模型输出 |
| Guardrails | 安全护栏 | 04/11 | 防止 AI 产生有害输出的防护机制 |
| GQA | 分组查询注意力 | 09 | Grouped-Query Attention |

### H

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| Handoff | 任务移交 | 02/03 | OpenAI Agents SDK 三原语之一 |
| Hallucination | 幻觉 | 06/11 | 模型编造看似合理但不真实的内容 |
| HITL | 人在回路 | 03 | Human-In-The-Loop,关键决策由人确认 |
| Higress | Higress | 10 | 阿里开源的 AI 网关,基于 Envoy |
| HippoRAG | 海马体 RAG | 08 | 模拟人类海马体记忆机制 |
| HNSW | 层次导航小世界图 | 08 | 最常用的 ANN 索引算法 |
| Hooks | 生命周期钩子 | 04 | Agent 事件触发时执行的确定性脚本 |
| Host | 宿主应用 | 02 | 运行 LLM 的应用本体 |
| HPA | 水平 Pod 自动扩缩 | 10 | Horizontal Pod Autoscaler |
| HHH | HHH 原则 | 11 | Helpful + Honest + Harmless |
| HyDE | 假设文档嵌入 | 08 | Hypothetical Document Embeddings |
| Hybrid Search | 混合检索 | 08 | 向量检索 + 关键词检索融合 |

### I

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| IDE | 集成开发环境 | 01 | 如 VS Code、JetBrains 系列 |
| Index | 索引 | 08 | 加速向量相似度搜索的数据结构 |
| In-Context Learning | 上下文学习 | 06 | 从提示中的示例学习,无需参数更新 |
| Inference Server | 推理服务 | 10 | 加载模型并提供推理 API 的服务 |
| inputSchema | 输入参数 Schema | 04 | JSON Schema 定义工具参数 |
| Interpretability | 可解释性 | 11 | 理解模型决策过程 |
| INT8/INT4 | 整数量化精度 | 09 | 8/4 位整数精度 |
| Iteration | 迭代 | 05 | 多轮循环优化 |
| IVF | 倒排文件索引 | 08 | 聚类后搜索的 ANN 算法 |

### J

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| Jailbreak | 越狱 | 11 | 绕过安全限制的高级注入 |
| JSON-RPC 2.0 | JSON 远程过程调用 | 02 | MCP 底层消息格式 |
| JWT | JSON Web Token | 10 | 自包含的 Token 格式 |

### K

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| KEDA | KEDA | 10 | 基于事件驱动的 K8s 自动扩缩 |
| Knowledge Graph | 知识图谱 | 07/08 | 实体-关系-实体的图结构知识库 |
| KTO | KTO 算法 | 09 | Kahneman-Tversky Optimization |
| KubeAI | KubeAI | 10 | K8s 上的模型部署平台 |
| KServe | KServe | 10 | K8s 上的模型推理标准 |
| KV Cache | KV 缓存 | 09/10 | 缓存 Attention 的 Key/Value 加速自回归 |

### L

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| Landlock | Linux 沙箱 | 01/04 | Linux 内核级沙箱机制 |
| Langfuse | Langfuse | 10 | 开源 LLM 可观测性平台 |
| LangGraph | LangGraph | 03 | LangChain 的图状态机 Agent 框架 |
| LangSmith | LangSmith | 10 | LangChain 的 LLM 可观测性平台 |
| LCEL | LangChain 表达语言 | 05 | 用管道符 `|` 组合组件 |
| Leaky Bucket | 漏桶 | 10 | 平滑输出的限流算法 |
| LLM | 大语言模型 | 09 | Large Language Model |
| LLM-as-a-Judge | LLM 评分 | 11 | 用另一个 LLM 评分 |
| LLMCompiler | LLM 编译器 | 05 | 并行执行多工具调用的 Plan 范式 |
| LiveBench | LiveBench | 11 | 持续更新的防污染基准 |
| LiveCodeBench | LiveCodeBench | 11 | 持续收集新题的代码基准 |
| llama.cpp | llama.cpp | 09/10 | C++ 实现的轻量 LLM 推理库 |
| Load Balancer | 负载均衡器 | 10 | 在多个后端实例间分配请求 |
| Logging | 日志 | 10 | 系统运行事件记录 |
| Long-term Memory | 长期记忆 | 07 | 跨会话的知识存储 |
| LoRA | 低秩适配 | 09 | Low-Rank Adaptation |
| Lost in the Middle | 中间丢失 | 09 | 长上下文中间信息利用率低 |

### M

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| Many-shot Jailbreak | 多样本越狱 | 11 | 长上下文用大量样本诱导 |
| Many-shot | 多样本 | 06 | 给大量示例(接近微调效果) |
| MATH | MATH | 11 | 竞赛级数学题基准 |
| Max Tokens | 最大 Token 数 | 06 | 限制输出长度的参数 |
| MBPP | MBPP | 11 | Mostly Basic Python Problems |
| MHA | 多头注意力 | 09 | Multi-Head Attention |
| MCP | 模型上下文协议 | 02 | Anthropic 开源的 Agent↔工具协议 |
| Mechanistic Interpretability | 机制可解释性 | 11 | 逆向工程神经网络内部机制 |
| MemGPT | MemGPT 系统 | 07 | 用 OS 思想管理 LLM 上下文 |
| Memory | 记忆 | 07 | Agent 的信息存储系统 |
| Metadata | 元数据 | 08 | 附加在向量上的结构化数据 |
| Metrics | 指标 | 10 | 可量化的运行数据 |
| MindIE | MindIE | 10 | 华为昇腾 NPU 推理引擎 |
| MLC-LLM | MLC-LLM | 10 | TVM Team 的跨平台 LLM |
| MMLU | MMLU | 11 | Massive Multitask Language Understanding |
| MMLU-Pro | MMLU-Pro | 11 | MMLU 升级版,10 选 1 |
| MMM | 多模态模型 | 09 | Multi-Modal Model |
| Moderation | 内容审核 | 11 | 对输入输出做安全审查 |
| Monitor | 监控 | 10 | 持续观察系统状态 |
| MoE | 混合专家模型 | 09 | Mixture of Experts |
| MQA | 多查询注意力 | 09 | Multi-Query Attention |
| MLA | 多头潜在注意力 | 09 | Multi-head Latent Attention |
| Multi-Agent | 多智能体 | 03 | 多个有不同角色的 Agent 协作 |

### N

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| Naive RAG | 朴素 RAG | 08 | 最基础的 RAG |
| NeMo Guardrails | NeMo 护栏 | 11 | NVIDIA 开源的 LLM 护栏框架 |
| NIST AI RMF | NIST AI 风险管理框架 | 11 | 美国 AI 风险管理标准 |
| Notification | 通知 | 02 | JSON-RPC 中无 ID 不需响应的消息 |

### O

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| OAuth 2.1 | OAuth 2.1 | 02/10 | OAuth 2.0 整合 + PKCE 强制 |
| OpenAI Moderation API | OpenAI 审核 API | 11 | 免费内容审核服务 |
| OneAPI | OneAPI | 10 | 开源 AI API 统一管理平台 |
| Ollama | Ollama | 10 | 本地一键运行开源 LLM 的工具 |
| ORPO | ORPO 算法 | 09 | Odds Ratio Preference Optimization |
| Orchestrator | 编排器 | 03/05 | 负责任务分配与汇总的组件/Agent |
| Orchestrator-Workers | 编排-工人 | 05 | 中央编排 LLM 动态拆分任务 |
| Overlap | 重叠 | 08 | 相邻块间保留的重叠区域 |
| OWASP LLM Top 10 | OWASP LLM 十大风险 | 11 | LLM 应用十大安全风险 |

### P

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| Pass@k | Pass@k | 11 | k 次尝试至少一次通过 |
| PagedAttention | 分页注意力 | 10 | 借鉴 OS 虚拟内存管理 KV Cache |
| PEFT | 参数高效微调 | 09 | Parameter-Efficient Fine-Tuning |
| Permission | 权限 | 04 | Agent 可操作资源的边界 |
| Persona | 人格 | 07 | Agent 的个性、偏好、知识结构 |
| Perspective API | Perspective API | 11 | Google 的有害内容检测 API |
| PII | 个人身份信息 | 11 | Personally Identifiable Information |
| PKCE | 密钥交换证明 | 02/10 | 防止授权码拦截的扩展 |
| Plan | 计划 | 03/05 | 拆解任务、规划步骤 |
| Plugin | 插件 | 04 | 可包含代码的可插拔扩展模块 |
| PQ | 乘积量化 | 08 | Product Quantization,向量压缩 |
| PP | 流水线并行 | 10 | Pipeline Parallelism,按层切分到多 GPU |
| Pre-training | 预训练 | 09 | 大规模无监督语料训练基础模型 |
| PreToolUse | 工具调用前钩子 | 04 | 工具调用前触发,可拦截 |
| Prefix Cache | 前缀缓存 | 10 | 共享相同前缀的 KV Cache |
| Prefix Tuning | 前缀微调 | 09 | 在输入前加可训练前缀 |
| Primitives | 协议原语 | 02 | MCP 预定义的操作类型 |
| Priority Queue | 优先级队列 | 05 | 按优先级排序的任务队列 |
| Procedure Memory | 程序记忆 | 07 | 记录如何做事的技能记忆 |
| Process | 流程 | 03 | CrewAI 中定义 Agent 协作顺序 |
| Prompt | 提示词 | 06 | 给 LLM 的输入指令 |
| Prompt Caching | 提示缓存 | 10 | 缓存重复前缀降低成本 |
| Prompt Chaining | 提示链 | 05 | 多个 LLM 调用串行执行 |
| Prompt Engineering | 提示工程 | 06 | 设计与优化提示词的学科 |
| Prompt Injection | 提示注入 | 11 | 构造特殊输入诱使模型忽略指令 |
| Prompt Template | 提示模板 | 06 | 可复用的提示结构 |
| Prompts | 提示词模板 | 02 | 用户触发的预定义交互模板 |
| Prometheus | Prometheus | 10 | 指标采集与存储系统 |
| Procedural Memory | 程序记忆 | 07 | 记录如何做事的技能记忆 |

### Q

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| QLoRA | 量化 LoRA | 09 | 4bit 量化 + LoRA |
| QPS | 每秒查询数 | 10 | Queries Per Second |
| Query Rewriting | 查询改写 | 08 | 用 LLM 改写用户查询 |
| Quantization | 量化 | 09 | 降低数值精度,省显存加速 |

### R

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| Rate Limit | 限流 | 10 | 限制请求速率,保护后端 |
| RAG | 检索增强生成 | 07/08 | Retrieval-Augmented Generation |
| RAGAS | RAG 评估框架 | 08 | RAG 系统评估指标框架 |
| Routing | 路由分发 | 05 | 先分类再路由到不同专用流程 |
| RAPTOR | 树状分层 RAG | 08 | Recursive Abstractive Processing |
| ReWOO | ReWOO | 05 | Reasoning WithOut Observation |
| RoPE | 旋转位置编码 | 09 | Rotary Position Embedding |
| ReAct | 推理+行动 | 03/05/06 | Reasoning + Acting 交替 |
| Red Team | 红队 | 11 | 模拟攻击者发现系统漏洞 |
| Reflection | 反思 | 03/06 | 执行后自我评估并改进 |
| Refinement | 细化 | 05 | 从粗到精的迭代模式 |
| Resources | 资源 | 02 | 用户主导访问的只读上下文数据 |
| Resource Template | 资源模板 | 02 | 带参数的 URI 模板 |
| Retrieval | 检索 | 08 | 从知识库找最相关文档的过程 |
| Reranker | 重排器 | 08 | 对初检结果二次排序 |
| RLHF | 人类反馈强化学习 | 09/11 | 对齐人类偏好 |
| RLAIF | AI 反馈强化学习 | 09/11 | 用 AI 替代人类标注偏好 |
| RMSNorm | RMS 归一化 | 09 | 只除 RMS,不减均值 |
| Roots | 根目录 | 02 | Client 向 Server 声明的文件边界 |
| Routing | 路由分发 | 05 | 先分类再路由到不同处理流程 |

### S

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| SAE | 稀疏自编码器 | 11 | Sparse Autoencoder,可解释性工具 |
| Sandbox | 沙箱 | 01/04 | 隔离的代码执行环境 |
| Sandboxing | 沙箱化 | 04 | 把不可信代码放入隔离环境执行 |
| Sampling | 采样原语 | 02 | Server 反向请求 Client 端 LLM |
| Safetensors | 安全张量格式 | 09 | HuggingFace 推荐的权重格式 |
| Scalable Oversight | 可扩展监督 | 11 | 用 AI 协助监督 AI |
| Scheduler | 调度器 | 05 | 决定任务执行顺序与时机的组件 |
| Scratchpad | 工作记忆区 | 03/07 | Agent 记录中间思考的临时区 |
| SFT | 监督微调 | 09 | Supervised Fine-Tuning |
| SGLang | SGLang | 10 | LMSYS 的结构化生成推理框架 |
| Seatbelt | macOS 沙箱 | 01/04 | macOS 内核级沙箱机制 |
| Self-Attention | 自注意力 | 09 | 序列内每个位置关注所有其他位置 |
| Self-Correction | 自我纠错 | 06 | 发现错误后自主修正 |
| Self-Consistency | 自我一致性 | 06 | 多次采样取多数答案 |
| Self-RAG | 自反思 RAG | 08 | LLM 自主决定是否检索 |
| Semantic Cache | 语义缓存 | 10 | 按语义相似度命中缓存 |
| Semantic Memory | 语义记忆 | 07 | 记录概念和事实的知识 |
| SentencePiece | 分词库 | 09 | Google 开源的多语言分词库 |
| Server | 协议服务端 | 02 | 暴露 Tools/Resources/Prompts 的进程 |
| Session | 会话 | 07 | 一次连续的交互过程 |
| Session ID | 会话标识 | 07 | 唯一标识一个会话的 ID |
| Short-term Memory | 短期记忆 | 07 | 当前会话的上下文 |
| Sliding Window | 滑动窗口 | 07 | 只保留最近 N 条消息的策略 |
| Skill | 技能 | 04 | 可复用的能力包 |
| Soft Constraint | 软约束 | 04 | 提示级规则,非 100% 强制 |
| Speculative Decoding | 推测解码 | 09/10 | 小模型猜,大模型验证 |
| Splitter | 分割器 | 08 | 实现分块的工具 |
| SSE | 服务器推送事件 | 02 | Server 单向推送消息的 HTTP 长连接 |
| State | 状态 | 07 | Agent 当前工作状态 |
| State Machine | 状态机 | 07 | 显式状态转移模型 |
| StateGraph | 状态图 | 03 | LangGraph 中用图结构表示的状态机 |
| Stop Sequence | 停止序列 | 06 | 遇到该字符串时停止生成 |
| Streamable HTTP | 流式 HTTP | 02 | 远程 Server 传输方式 |
| Streaming | 流式输出 | 01/09 | 边生成边输出,实时显示 |
| STT | 语音转文字 | 01 | 同 ASR |
| Subagent | 子智能体 | 03 | 主 Agent 委派任务的专用 Agent |
| Summarization | 摘要压缩 | 07 | 对早期消息做摘要 |
| Supervisor | 主管智能体 | 03 | 监督其他 Agent 执行质量 |
| SWE-bench | SWE-bench | 11 | 真实 GitHub Issue 修复评估 |
| SwiGLU | SwiGLU 激活 | 09 | Swish + Gate,Llama 等采用 |

### T

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| τ-bench | Tau-Bench | 11 | 模拟真实工作场景的 Agent 评估 |
| Tasks | 任务原语 | 02 | 持久化执行包装(实验性) |
| Task Decomposition | 任务拆解 | 05 | 把复杂任务分解为子任务 |
| Temperature | 温度 | 06 | 控制输出随机性的参数 |
| TensorRT-LLM | TRT-LLM | 10 | NVIDIA 的 LLM 推理优化引擎 |
| TGI | 文本生成推理 | 10 | HuggingFace 推理服务框架 |
| tiktoken | tiktoken | 09 | OpenAI 的 BPE 分词库 |
| ToT | 思维树 | 06 | Tree of Thoughts,探索多条推理路径 |
| Token | 词元 | 09 | LLM 处理文本的最小单位 |
| Tokenizer | 分词器 | 09 | 把文本切分为 Token 的工具 |
| Token Bucket | 令牌桶 | 10 | 允许突发的限流算法 |
| Top-k | Top-k 采样 | 06 | 只从概率最高的 k 个 token 中采样 |
| Top-p | 核采样 | 06 | 限制采样范围的参数(累积概率) |
| Top-K | 前 K 个 | 08 | 返回最相关的 K 个结果 |
| Topological Sort | 拓扑排序 | 05 | 对 DAG 节点进行线性排序 |
| Tool Calling | 工具调用 | 03/04 | LLM 调用外部工具的能力 |
| Tool Schema | 工具描述规范 | 04 | 描述工具名称/功能/参数的 JSON Schema |
| Tool Annotation | 工具注释 | 04 | MCP 工具的元数据(只读/破坏性/幂等) |
| Toolformer | 工具专用模型 | 09 | Meta 提出,模型自主学会用工具 |
| Toxicity | 毒性 | 11 | 有害、攻击性内容 |
| TP | 张量并行 | 10 | Tensor Parallelism,层内切分到多 GPU |
| TPOT | 每 Token 延迟 | 10 | Time Per Output Token |
| Transformer | Transformer 架构 | 09 | 基于 Attention 的神经网络架构 |
| Trigger | 触发器 | 05 | 启动工作流的事件或条件 |
| TruthfulQA | TruthfulQA | 11 | 检测模型是否模仿人类误区 |
| TTS | 语音合成 | 01 | 将文字转换为语音 |
| TTFT | 首 Token 延迟 | 10 | Time To First Token |

### U-V

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| User Prompt | 用户提示 | 06 | 用户每轮的具体任务指令 |
| Vector Database | 向量数据库 | 07/08 | 专门存储和检索向量的数据库 |
| VLM | 视觉语言模型 | 09 | Vision Language Model |

### W-X-Y-Z

| 术语 | 中文 | 章节 | 一句话解释 |
|------|------|------|-----------|
| Webhook | 网络钩子 | 05 | 事件驱动的反向 HTTP 回调 |
| WebUI | 网页用户界面 | 01 | 在浏览器中运行的图形化交互界面 |
| Whisper | OpenAI ASR 模型 | 01 | 支持 99 种语言的开源 ASR |
| Widget | 嵌入式组件 | 01 | 嵌入到其他应用中的轻量 AI UI 组件 |
| Working Memory | 工作记忆 | 07 | Agent 当前任务的临时工作区 |
| Workflow | 工作流 | 03/05 | 通过预定义代码路径编排 LLM 与工具 |
| Zero-shot | 零样本 | 06 | 不给示例,直接要求模型完成任务 |
| Zero-shot CoT | 零样本思维链 | 06 | 加 "Let's think step by step" |
| 生成式 AI 管理办法 | 生成式 AI 管理办法 | 11 | 中国生成式 AI 服务监管 |
| ISO/IEC 42001 | ISO 42001 | 11 | AI 管理体系国际标准 |

---

## 六、技术栈全景图

```
┌────────────────────────────────────────────────────────────────────────────┐
│                                                                            │
│              🛠️ AI 全栈技术栈全景图(2026-07)                              │
│                                                                            │
│  [用户接入层]                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ CLI: Codex CLI / Claude Code / Gemini CLI / Qwen Code              │    │
│  │ IDE: Cursor / Windsurf / Copilot / Continue / Cline                │    │
│  │ WebUI: ChatGPT / Claude.ai / Gemini / OpenWebUI / LobeChat         │    │
│  │ 语音: Whisper / MeloTTS / OpenVoice / Deepgram                     │    │
│  │ SDK: OpenAI SDK / Anthropic SDK / Vercel AI SDK / LangChain        │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                  ▼                                         │
│  [Agent 框架层]                                                            │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ LangGraph / CrewAI / OpenAI Agents SDK / AutoGen / DSPy /          │    │
│  │ LlamaIndex / smolagents / Pydantic AI / Mastra / Atomic Agents     │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                  ▼                                         │
│  [协议与标准层]                                                            │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ MCP(Anthropic 2024-11)/ A2A(Google 2025-04)/                    │    │
│  │ Function Calling(OpenAI 2023-06)/ AGENTS.md / AgentSkills.io     │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                  ▼                                         │
│  [模型层 - 闭源]                                                           │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ GPT-4o / GPT-5 / Claude 4 (Opus/Sonnet) / Gemini 2.5 / Grok       │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                  ▼                                         │
│  [模型层 - 开源]                                                           │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ Llama 4 / DeepSeek-V3/R1 / Qwen 3 / Mistral / Mixtral / GLM-4.5 / │    │
│  │ Phi-4 / Gemma 3 / Yi / Command R+                                  │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                  ▼                                         │
│  [RAG / 知识层]                                                            │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ 向量库: Milvus / Qdrant / Weaviate / Chroma / Pinecone / PGVector │    │
│  │ Embedding: BGE / text-embedding-3 / Cohere / Jina                  │    │
│  │ Reranker: BGE-Reranker / Cohere Rerank / Jina Reranker             │    │
│  │ 框架: LangChain / LlamaIndex / Haystack / DSPy                     │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                  ▼                                         │
│  [推理引擎层]                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ vLLM / TGI / Ollama / TensorRT-LLM / SGLang / llama.cpp /          │    │
│  │ LMDeploy / DeepSpeed-FastGen / MLC-LLM / MindIE(华为)             │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                  ▼                                         │
│  [网关与运维层]                                                            │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ 网关: OneAPI / LiteLLM / Higress / New API / Portkey               │    │
│  │ 编排: Kubernetes / Docker / KubeAI / KServe / Ray                  │    │
│  │ 伸缩: HPA / KEDA / Cluster Autoscaler                              │    │
│  │ 监控: Prometheus / Grafana / LangSmith / Langfuse / OpenTelemetry  │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                  ▼                                         │
│  [安全与评估层]                                                            │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ 护栏: NeMo Guardrails / Llama Guard / Guardrails AI / Llama Prompt │    │
│  │ 审核: OpenAI Moderation / Perspective API / 中文审核               │    │
│  │ 评估: OpenCompass / lm-eval-harness / RAGAS / Promptfoo            │    │
│  │ 红队: Garak / PyRIT / HarmBench                                    │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 七、应用场景对照表

> "我要做 X,应该读哪几章?" 速查表。

| 应用场景 | 必读章节 | 关键工具/技术 |
|---------|---------|--------------|
| **构建 CLI Agent** | 01 + 03 + 04 + 05 | Codex CLI / Claude Code / Skills / Hooks |
| **集成外部工具(API/DB)** | 02 + 04 | MCP Server / Function Calling / Tool Schema |
| **多 Agent 协作系统** | 03 + 05 + 02 | LangGraph / CrewAI / A2A / Handoff |
| **企业知识库问答** | 08 + 07 + 06 | RAG / Milvus / BGE / Reranker |
| **代码生成助手** | 01 + 06 + 09 | Cursor / Claude Code / CoT |
| **本地部署 LLM** | 10 + 09 | Ollama / vLLM / llama.cpp / GGUF |
| **生产 LLM 服务** | 10 + 11 | vLLM + OneAPI + Prometheus + Guardrails |
| **多模型路由 / 成本优化** | 10 | OneAPI / LiteLLM / 智能路由 |
| **评估模型能力** | 11 | MMLU / HumanEval / SWE-bench / Arena |
| **AI 安全合规** | 11 | NeMo Guardrails / 红队 / EU AI Act |
| **客服对话机器人** | 01 + 03 + 07 + 08 | Chatbot / Agent / Memory / RAG |
| **AI 编程 Copilot** | 01 + 06 + 04 | IDE 插件 / Composer / Cascade |
| **长文档分析** | 06 + 08 + 09 | Long Context / RAG / Claude Opus |
| **语音助手** | 01 + 03 | Whisper / MeloTTS / ASR + TTS |
| **AI Agent 测试平台** | 11 + 03 | AgentBench / τ-bench / GAIA |

---

## 八、推荐工具清单(按场景)

### 8.1 CLI Agent(命令行 AI 编程)

| 工具 | 厂商 | 特点 | 适用场景 |
|------|------|------|---------|
| **Codex CLI** | OpenAI | 11 大终端工作流,审批模式 | 通用编程 |
| **Claude Code** | Anthropic | 内置 Subagent,Skills,Hooks | 复杂项目 |
| **Gemini CLI** | Google | Gemini 2.5 集成 | Google 生态 |
| **Qwen Code** | 阿里 | Qwen 3 集成 | 中文场景 |

### 8.2 IDE 集成

| 工具 | 厂商 | 特点 |
|------|------|------|
| **Cursor** | Anysphere | Composer 多文件编辑 |
| **Windsurf** | Codeium | Cascade 任务级流 |
| **GitHub Copilot** | GitHub/MS | VS Code 原生 |
| **Continue** | Continue Dev | 开源可定制 |
| **Cline** | Cline | VS Code 插件 |

### 8.3 Agent 框架

| 框架 | 厂商 | 特点 |
|------|------|------|
| **LangGraph** | LangChain | 图状态机,可控性强 |
| **CrewAI** | CrewAI Inc. | 角色扮演,易用 |
| **OpenAI Agents SDK** | OpenAI | 三原语 + Tracing |
| **AutoGen** | Microsoft | 多 Agent 对话 |
| **DSPy** | Stanford | 提示编程 |
| **LlamaIndex** | LlamaIndex | RAG + Agent |

### 8.4 推理引擎

| 引擎 | 适用场景 | 关键特性 |
|------|---------|---------|
| **vLLM** | 生产高吞吐 | PagedAttention |
| **TGI** | HF 生态 | 稳定 |
| **Ollama** | 本地开发 | 简单易用 |
| **TensorRT-LLM** | NVIDIA 极致性能 | NVIDIA 优化 |
| **SGLang** | 结构化生成 | RadixAttention |
| **llama.cpp** | 边缘/CPU | GGUF 量化 |

### 8.5 向量数据库

| 数据库 | 特点 | 适用场景 |
|--------|------|---------|
| **Milvus** | 分布式,大规模 | 企业生产 |
| **Qdrant** | Rust 实现,高性能 | 通用 |
| **Weaviate** | 内置模块化 | 多模态 |
| **Chroma** | 轻量易用 | 原型 |
| **Pinecone** | 云托管 | 无运维 |
| **PGVector** | PostgreSQL 扩展 | 已有 PG |

### 8.6 网关

| 网关 | 特点 |
|------|------|
| **OneAPI** | 开源,多模型统一 |
| **LiteLLM** | Python 库 + Proxy,100+ 模型 |
| **Higress** | 阿里开源,基于 Envoy |
| **New API** | OneAPI 衍生 |
| **Portkey** | 商业,全功能 |

---

## 九、经典必读论文 / 文章 / 白皮书

### 9.1 基础论文(必读)

| 论文 | 年份 | 重要性 | 链接 |
|------|------|--------|------|
| **Attention Is All You Need** | 2017 | ⭐⭐⭐⭐⭐ | https://arxiv.org/abs/1706.03762 |
| **GPT-3: Language Models are Few-Shot Learners** | 2020 | ⭐⭐⭐⭐⭐ | https://arxiv.org/abs/2005.14165 |
| **InstructGPT (RLHF)** | 2022 | ⭐⭐⭐⭐⭐ | https://arxiv.org/abs/2203.02155 |
| **LoRA** | 2021 | ⭐⭐⭐⭐⭐ | https://arxiv.org/abs/2106.09685 |
| **QLoRA** | 2023 | ⭐⭐⭐⭐ | https://arxiv.org/abs/2305.14314 |
| **Constitutional AI** | 2022 | ⭐⭐⭐⭐ | https://arxiv.org/abs/2212.08073 |
| **DPO** | 2023 | ⭐⭐⭐⭐ | https://arxiv.org/abs/2305.18290 |

### 9.2 Agent 经典论文

| 论文 | 年份 | 重要性 | 链接 |
|------|------|--------|------|
| **ReAct** | 2022 | ⭐⭐⭐⭐⭐ | https://arxiv.org/abs/2210.03629 |
| **Reflexion** | 2023 | ⭐⭐⭐⭐ | https://arxiv.org/abs/2303.11366 |
| **Toolformer** | 2023 | ⭐⭐⭐⭐ | https://arxiv.org/abs/2302.04761 |
| **Generative Agents(斯坦福小镇)** | 2023 | ⭐⭐⭐⭐⭐ | https://arxiv.org/abs/2304.03442 |
| **MemGPT** | 2023 | ⭐⭐⭐⭐ | https://arxiv.org/abs/2310.08560 |
| **Voyager(Minecraft Agent)** | 2023 | ⭐⭐⭐ | https://arxiv.org/abs/2305.16291 |

### 9.3 RAG 经典论文

| 论文 | 年份 | 重要性 | 链接 |
|------|------|--------|------|
| **RAG 原始论文** | 2020 | ⭐⭐⭐⭐⭐ | https://arxiv.org/abs/2005.11401 |
| **GraphRAG(微软)** | 2024 | ⭐⭐⭐⭐ | https://arxiv.org/abs/2404.16130 |
| **RAPTOR** | 2024 | ⭐⭐⭐⭐ | https://arxiv.org/abs/2401.18059 |
| **Self-RAG** | 2023 | ⭐⭐⭐⭐ | https://arxiv.org/abs/2310.11511 |
| **CRAG** | 2024 | ⭐⭐⭐ | https://arxiv.org/abs/2401.15884 |
| **HippoRAG** | 2024 | ⭐⭐⭐ | https://arxiv.org/abs/2405.14831 |

### 9.4 推理优化论文

| 论文 | 年份 | 重要性 | 链接 |
|------|------|--------|------|
| **FlashAttention** | 2022 | ⭐⭐⭐⭐⭐ | https://arxiv.org/abs/2205.14135 |
| **vLLM / PagedAttention** | 2023 | ⭐⭐⭐⭐⭐ | https://arxiv.org/abs/2309.06180 |
| **Speculative Decoding** | 2023 | ⭐⭐⭐⭐ | https://arxiv.org/abs/2302.01318 |
| **Mixture of Experts(MoE)** | 2022 | ⭐⭐⭐⭐⭐ | https://arxiv.org/abs/2209.01667 |
| **DeepSeek-V2(MLA)** | 2024 | ⭐⭐⭐⭐ | https://arxiv.org/abs/2405.04434 |

### 9.5 评估与安全论文

| 论文 | 年份 | 重要性 | 链接 |
|------|------|--------|------|
| **MMLU** | 2021 | ⭐⭐⭐⭐⭐ | https://arxiv.org/abs/2009.03300 |
| **HumanEval** | 2021 | ⭐⭐⭐⭐⭐ | https://arxiv.org/abs/2107.03374 |
| **GSM8K** | 2021 | ⭐⭐⭐⭐⭐ | https://arxiv.org/abs/2110.14168 |
| **TruthfulQA** | 2022 | ⭐⭐⭐⭐ | https://arxiv.org/abs/2109.07958 |
| **SWE-bench** | 2023 | ⭐⭐⭐⭐ | https://arxiv.org/abs/2310.06770 |
| **OWASP LLM Top 10** | 2025 | ⭐⭐⭐⭐⭐ | https://owasp.org/www-project-top-10-for-large-language-model-applications/ |

### 9.6 厂商实践文章

| 文章 | 厂商 | 链接 |
|------|------|------|
| **Building Effective Agents** | Anthropic | https://www.anthropic.com/research/building-effective-agents |
| **构建智能体实践指南** | OpenAI | https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf |
| **NSA MCP 安全指南(2026-05)** | NSA AISC | https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/nsa-releases-security-design-considerations-for-ai-driven-automation-leveraging/ |
| **Effective Context Engineering** | Anthropic | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| **Multi-Agent Orchestration** | OpenAI | https://openai.com/index/new-tools-for-building-agents/ |

---

## 十、快速入口(官方文档)

### 10.1 协议与标准

- **MCP 官网:** https://modelcontextprotocol.io
- **MCP 规范:** https://spec.modelcontextprotocol.io/
- **A2A GitHub:** https://github.com/google/A2A
- **AGENTS.md:** https://agents.md
- **AgentSkills.io:** https://agentskills.io

### 10.2 厂商文档

| 厂商 | 链接 |
|------|------|
| OpenAI | https://platform.openai.com/docs |
| Anthropic | https://docs.anthropic.com/ |
| Claude Code | https://code.claude.com/docs |
| Codex CLI | https://developers.openai.com/codex/cli |
| Google AI | https://ai.google.dev/ |
| Google A2A | https://google.github.io/A2A/ |
| Meta Llama | https://llama.meta.com/ |
| DeepSeek | https://api-docs.deepseek.com/ |
| Qwen(通义千问) | https://help.aliyun.com/zh/dashscope/ |

### 10.3 框架与工具

| 工具 | 链接 |
|------|------|
| LangGraph | https://langchain-ai.github.io/langgraph/ |
| CrewAI | https://docs.crewai.com/ |
| DSPy | https://dspy.ai/ |
| LlamaIndex | https://docs.llamaindex.ai/ |
| AutoGen | https://microsoft.github.io/autogen/ |
| vLLM | https://docs.vllm.ai/ |
| Ollama | https://ollama.com/ |
| TGI | https://huggingface.co/docs/text-generation-inference/ |
| TensorRT-LLM | https://nvidia.github.io/TensorRT-LLM/ |
| SGLang | https://docs.sglang.ai/ |
| llama.cpp | https://github.com/ggerganov/llama.cpp |
| OneAPI | https://github.com/songquanpeng/one-api |
| LiteLLM | https://docs.litellm.ai/ |
| Milvus | https://milvus.io/docs |
| Qdrant | https://qdrant.tech/documentation/ |
| Weaviate | https://weaviate.io/developers/weaviate |
| Chroma | https://docs.trychroma.com/ |
| Langfuse | https://langfuse.com/docs |
| NeMo Guardrails | https://docs.nvidia.com/nemo/guardrails/ |
| Llama Guard | https://llama.meta.com/docs/model-cards-and-prompt-formats/llama-guard-3/ |
| OpenCompass | https://opencompass.org.cn/ |
| lm-eval-harness | https://github.com/EleutherAI/lm-evaluation-harness |

### 10.4 法规与标准

| 法规/标准 | 链接 |
|----------|------|
| 中国生成式 AI 管理办法 | http://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm |
| EU AI Act | https://artificialintelligenceact.eu/ |
| US EO 14110 | https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/ |
| NIST AI RMF | https://www.nist.gov/itl/ai-risk-management-framework |
| ISO/IEC 42001 | https://www.iso.org/standard/81230.html |
| GDPR | https://gdpr-info.eu/ |

---

## 十一、常见问题 FAQ

### Q1: 我刚入门 AI,应该从哪开始?

**A:** 按路径 A(递进式):先读 `09 底层模型`了解 LLM 是什么,再读 `06 提示推理`学会用 Prompt,然后 `03 智能体主体`了解 Agent。

### Q2: 我要做 CLI Agent,需要读哪几章?

**A:** 必读 `01 交互入口` + `03 智能体主体` + `04 能力约束` + `05 任务编排`。如果要用 MCP 接工具,加 `02 通信协议`。

### Q3: vLLM 和 Ollama 怎么选?

**A:** 生产高吞吐用 vLLM(见 `10 部署运维`);本地开发/个人用 Ollama(更简单)。

### Q4: MCP 和 Function Calling 什么关系?

**A:** Function Calling 是 OpenAI 2023-06 的 LLM 调外部函数机制(原始);MCP 是 Anthropic 2024-11 开源的标准化协议,把 M×N 集成降为 M+N。详见 `02 通信协议`。

### Q5: CLAUDE.md、AGENTS.md、Rules、Hooks 有什么区别?

**A:** 
- **CLAUDE.md:** Claude Code 项目级软规则(LLM 读)
- **AGENTS.md:** 跨 CLI 工具通用标准(60k+ 项目采用)
- **Rules:** Host 程序强制执行的约束
- **Hooks:** 事件触发的确定性脚本(100% 强制)

详见 `04 能力与约束体系`。

### Q6: 我要部署企业 LLM 服务,怎么开始?

**A:** 按 `10 部署运维` 的"生产部署最佳实践"章节:① 选模型 → ② 选推理引擎 → ③ 用 Docker/K8s 部署 → ④ 加网关(OneAPI/LiteLLM)→ ⑤ 加监控(Prometheus+Grafana)→ ⑥ 加护栏(NeMo Guardrails)。

### Q7: RAG 怎么选向量库?

**A:** 见 `08 RAG 知识库体系`:
- 原型:Chroma
- 生产通用:Qdrant / Milvus
- 已有 PostgreSQL:PGVector
- 云托管:Pinecone

### Q8: 怎么评估我的 LLM 应用?

**A:** 见 `11 安全对齐评估`:
- 通用能力:MMLU / MMLU-Pro
- 代码:HumanEval / SWE-bench
- 数学:GSM8K / MATH
- Agent:AgentBench / τ-bench
- 防污染:LiveBench
- 人类偏好:LMSYS Arena
- 自动化:LLM-as-a-Judge
- 红队:Garak / PyRIT

### Q9: 微调选 LoRA 还是 QLoRA?

**A:** 见 `09 底层大模型底座`:
- 显存够:LoRA(质量更好)
- 显存紧张:QLoRA(4bit 量化,极致省显存)
- 都属于 PEFT(参数高效微调)

### Q10: 怎么防止 Prompt Injection?

**A:** 见 `11 安全对齐评估`:
- Input Guardrails(输入护栏)
- Llama Prompt Guard
- 结构化 Prompt(分离指令与数据)
- 最小权限原则
- OWASP LLM Top 10 防御

---

## 十二、学习心法与方法论

### 12.1 三遍学习法

```
第 1 遍:通读(建立印象)
  - 跳过代码,只看概念和图表
  - 在词汇表标记陌生术语

第 2 遍:精读(理解原理)
  - 带着问题读
  - 动手跑代码示例
  - 做笔记

第 3 遍:实践(内化能力)
  - 做一个小项目
  - 教给别人(Feynman 技巧)
```

### 12.2 学习顺序原则

```
概念先行,实践跟上,项目内化

  ① 看懂概念 ──► ② 跑通 Demo ──► ③ 改造实践 ──► ④ 创造项目
       ↑                                              │
       └──────────── 遇到问题回查 ◄──────────────────┘
```

### 12.3 知识体系构建原则

| 原则 | 说明 |
|------|------|
| **从顶向下** | 先看全貌(本 README),再深入各章 |
| **从底向上** | 先理解基础(09 模型),再向上构建 |
| **横向对照** | 多个相似概念对比(如 vLLM vs TGI vs TRT-LLM) |
| **纵向追溯** | 遇到术语向上查章节,向下查论文 |
| **实践验证** | 每学一个概念,跑一遍代码 |

### 12.4 常见误区

```
❌ 误区 1: 直接学 Agent 框架,不学底层
   ✅ 正确: 先理解 LLM 基础(09),再学 Agent(03)

❌ 误区 2: 死记硬背术语
   ✅ 正确: 用代码跑一遍,理解其作用

❌ 误区 3: 追求"最新最强"模型
   ✅ 正确: 先用小模型(Llama 3 8B)跑通,再上大模型

❌ 误区 4: 不看官方文档,只看博客
   ✅ 正确: 官方文档是源头,博客是补充

❌ 误区 5: 只学不用
   ✅ 正确: 边学边做项目
```

### 12.5 推荐项目实践

| 难度 | 项目 | 涉及章节 |
|------|------|---------|
| ⭐ | 用 Ollama 跑本地 LLM | 10 |
| ⭐⭐ | 写一个 MCP Server | 02 |
| ⭐⭐ | 用 LangGraph 做单 Agent | 03 + 05 |
| ⭐⭐⭐ | 企业知识库 RAG | 08 + 07 |
| ⭐⭐⭐ | 多 Agent 协作系统 | 03 + 05 + 02 |
| ⭐⭐⭐⭐ | 用 vLLM 部署生产服务 | 10 + 11 |
| ⭐⭐⭐⭐ | CLI Agent(类 Claude Code) | 01 + 03 + 04 + 05 |
| ⭐⭐⭐⭐⭐ | 端到端 AI 产品 | 全部 11 章 |

---

## 十三、学习前置要求

### 13.1 必备基础

- **命令行操作:** bash / PowerShell 基本命令
- **脚本语言:** Python(主)或 JavaScript(次)
- **LLM 概念:** 知道 ChatGPT 是什么,大致原理
- **Git:** 基本克隆/提交操作

### 13.2 推荐基础

- **Docker:** 容器化基础(用于部署)
- **REST API:** HTTP 协议基础
- **JSON:** 数据格式
- **Linux:** 基本操作(部署需要)

### 13.3 环境准备

| 工具 | 用途 | 安装 |
|------|------|------|
| **Python 3.10+** | 主语言 | https://python.org |
| **Node.js 20+** | CLI 工具 | https://nodejs.org |
| **Docker** | 容器部署 | https://docker.com |
| **Git** | 版本控制 | https://git-scm.com |
| **VS Code** | IDE | https://code.visualstudio.com |
| **Ollama** | 本地 LLM | https://ollama.com |
| **uv** | Python 包管理(推荐) | https://docs.astral.sh/uv/ |

---

## 十四、技术版本基准(2026-07)

| 技术/规范 | 版本/日期 | 说明 |
|----------|----------|------|
| **MCP 规范** | 2025-11-25(现行) | Tasks 原语(实验性)、URL 模式 Elicitation、CIMD、OIDC Discovery |
| **MCP 规范** | 2025-03-26 / 2025-06-18 | Streamable HTTP + OAuth 2.1(03-26);structuredContent、Elicitation(06-18) |
| **A2A 协议** | 2025-04 发布;1.0(2026) | Google 发起,Linux Foundation 托管 |
| **Codex CLI** | 持续更新(以官方 release 为准) | approval_policy × sandbox_mode 审批模型 |
| **Claude Code** | 持续更新(以官方 release 为准) | 内置 Explore/Plan/General-purpose 三种 Subagent |
| **OpenAI Agents SDK** | - | 三原语(Agents / Handoffs / Guardrails)+ Tracing |
| **AGENTS.md** | - | 60k+ 项目采用 |
| **主流框架** | - | LangGraph / CrewAI / DSPy / LlamaIndex |
| **推理引擎** | - | vLLM(PagedAttention)/ TGI / Ollama / TensorRT-LLM / SGLang |
| **主流 LLM** | - | GPT-5 / Claude 4 / Gemini 2.5 / Llama 4 / DeepSeek-V3/R1 / Qwen 3 |
| **OWASP LLM Top 10** | 2025 版 | 最新 LLM 应用安全风险 |
| **EU AI Act** | 2024-08 生效 | 全球首个综合 AI 监管法 |

---

## 十五、文档统计与版本日志

### 15.1 文档统计

| 章节 | 行数 | 术语数 | 图表数 | 代码示例 | 状态 |
|------|------|--------|--------|---------|------|
| 00 README | 本文件 | - | 6 | 0 | ✅ v4 |
| 01 交互入口 | ~1230 | 21 | 15+ | 25+ | ✅ v4 |
| 02 通信协议 | ~1940 | 30 | 30+ | 35+ | ✅ v4 |
| 03 智能体主体 | ~1370 | 30 | 20+ | 20+ | ✅ v4 |
| 04 能力与约束 | ~1230 | 30 | 15+ | 25+ | ✅ v4 |
| 05 任务编排 | ~2120 | 30 | 25+ | 30+ | ✅ v4 |
| 06 提示推理 | ~1820 | 30 | 20+ | 25+ | ✅ v4 |
| 07 记忆状态 | ~1720 | 30 | 20+ | 20+ | ✅ v4 |
| 08 RAG 体系 | ~2430 | 40 | 30+ | 35+ | ✅ v4 |
| 09 模型底座 | ~1860 | 50 | 25+ | 25+ | ✅ v4 |
| 10 部署运维 | ~2980 | 50 | 35+ | 45+ | ✅ v4 |
| 11 安全评估 | ~2460 | 50 | 30+ | 30+ | ✅ v4 |
| 12 Agent 对比(专题) | ~1020 | 20 | 15+(含 3 张自绘图) | 5+ | ✅ v4.1 |
| 13 自托管 Agent(专题) | ~810 | 18 | 27(含 2 张自绘图) | 10+ | ✅ v4.2 |
| 14 多模态 Agent(专题) | ~1010 | 39 | 30+ | 4(完整示例) | ✅ v4.3 |
| 15 构建自己的Agent(专题) | ~1138 | 45 | 40+ | 10+(双版本完整代码) | ✅ v4.4 |
| **合计** | **~25,700** | **513(速查表)** | **580+ 表格** | **590+ 代码块** | ✅ |

### 15.2 版本日志

#### v4.4(2026-07-22 第十五章完成)

- ✅ 第十五章《构建自己的Agent全流程》从 642 行扩展到 1138 行,正式完稿
  - 九阶段生命周期:需求定义→框架选型→架构设计→模型接入→工具设计→提示词工程→记忆与RAG→实战→评估→安全部署
  - 框架分析六维模型(生态/性能/学习曲线/调试体验/可扩展性/社区)与 7 大框架对比表+决策树
  - 单/多Agent架构设计:分层架构、Agent Loop 状态机、上下文工程
  - 模型接入层:能力分级、结构化输出、adapter 模式、容错与 fallback
  - 工具设计与 MCP 封装:四原则、Schema 写法、MCP Server 完整封装示例
  - 提示词工程:六段式模板、Few-shot 策略、版本管理、防注入
  - 记忆与 RAG 接入:四层记忆架构、最小 RAG 实现
  - 手写 vs LangGraph 双版本完整可运行实战代码
  - 评估与迭代闭环:自动化评估 pipeline、回归测试
  - 安全加固与部署上线:Docker 化、环境变量管理、速率限制、日志审计
  - 十大失败模式排查表(附症状、根因、修复方案)
- ✅ 第十四章"与本书其他章节的呼应"段落更新,加入第十五章实际内容描述
- ✅ README 统计更新:合计 ~25,700 行、513 速查术语、15 个章节

#### v4.3(2026-07-22 新增多模态笔记)

- ✅ 新增 `14-多模态Agent.md`(~1010 行,纯知识笔记体,不含价格/费用分析)
  - VLM 原理:LLaVA 三段式、图像 patch 与 token 技术账、CLIP/SigLIP 模态对齐
  - 视觉操作 Agent:截图-决策-动作循环、Visual Grounding、三条实现路径 + Playwright 实战
  - 语音模态:ASR/TTS 三段式 vs 端到端、全双工、延迟预算、faster-whisper 实战
  - 文档/视频理解、多模态 RAG、MCP 工具化封装、评估基准(MMMU/OSWorld/ScreenSpot 等)
  - 视觉/语音提示注入攻击链与防御;论文 arXiv 号全部经核实
- ✅ README 更新为"11 大类 + 3 专题";后续规划同步

#### v4.2(2026-07-22 新增自托管专题篇)

- ✅ 新增 `13-自托管个人Agent.md`(~810 行):OpenClaw(小龙虾)与 Hermes Agent(爱马仕)框架解读与正面对比
  - 花名/黑话与爆火现象解读(养虾/喂虾/放虾、代装服务产业链)
  - 架构深挖:共同范式(常驻进程 + Gateway + 全系统工具面)、Hermes 学习循环、OpenClaw 白盒哲学、消息全生命周期时序图
  - 部署实战(命令示例经官方 README 核实)、成本估算、Shell 级权限安全风险专节
  - 新增 `assets/agent-compare/` 两张自绘图:能力雷达 / 社区热度
- ✅ 12 章同步接入:3.3 自托管品类指引、2026 时间线、决策树与场景表
- ✅ README 索引更新为"11 大类 + 2 专题";后续规划章节号顺延

#### v4.1(2026-07-22 新增专题篇)

- ✅ 新增 `12-主流Agent对比分析.md`(~1010 行):2026-07 主流 AI Agent 全景对比与选型指南
  - 编程 Agent 产品深评:Claude Code / OpenAI Codex / Cursor / GitHub Copilot / Devin(Devin Desktop)/ Google Jules / Gemini CLI / 开源阵营(OpenCode/Aider/Cline 等)
  - 通用 Agent:ChatGPT Agent / Manus / Kimi 等形态对比
  - 开发框架对比:LangGraph 1.0 / CrewAI / OpenAI Agents SDK / Claude Agent SDK / Google ADK / Microsoft Agent Framework 1.0 / Pydantic AI V2 / LlamaIndex Workflows 1.0
  - 企业托管平台速览 + 2024→2026 格局演变 + 选型决策树与场景推荐
- ✅ 新增 `assets/agent-compare/` 三张自绘对比图(定位散点图 / 基准条形图 / 框架雷达图),matplotlib 生成,CJK 字体
- ✅ 全部事实(价格/基准/版本)以 2026-07 公开资料核实,文内含数据口径声明
- ✅ README 索引、统计、学习地图同步更新;后续规划章节号顺延

#### v4.0(2026-07 查缺补漏 + 实战化迭代)

**硬错误修复(70+ 处,读者照抄即报错/被误导的内容):**
- ✅ 02:MCP 版本表修正(Streamable HTTP 属 2025-03-26、structuredContent 属 2025-06-18、Tasks 属 2025-11-25);删除无法核实的"2026-07-28 RC";MCP server 启动代码、官方 Server 表、A2A 新版 API(message/send、contextId、agent-card.json)全部修正
- ✅ 01/04:Claude Code 权限模式、Hooks 三层嵌套配置与 stdin JSON 输入、SKILL.md 官方字段、Codex `approval_policy`/`sandbox_mode` 等"照抄即报错"配置全部按官方文档重写
- ✅ 03/05:OpenAI Agents SDK Guardrails、Anthropic 工具 schema、Airflow schedule、拼写错误(`anthropropic`)等代码错误修复;五处"官方示例"误导性归因改为"按官方思想改写"
- ✅ 08:GraphRAG 编造 API 改为官方 CLI 流程;Contextual Retrieval 数字统一为 49%→56%→67%;qdrant `query_points` 新 API
- ✅ 09/10:KV Cache 计算修正(GQA 口径,8B 模型 32k 上下文 ≈4.3GB);PagedAttention 统一为 arXiv 2309.06180;vLLM 多机部署改 Ray 集群正确流程;Prompt Caching 计费修正(写 1.25× / 读 0.1×);llama.cpp cmake 编译流
- ✅ 11:Llama Guard 判定逻辑、Prompt Guard 分类用法、τ-bench arXiv 号、假 DP-SGD 改 Opacus;NSA MCP 安全指南核实为真实文件并换官方链接
- ✅ 全库:chat.lmsys.org → lmarena.ai;不存在的型号(Llama 4 70B/8B)、张冠李戴的论文引用逐一修正

**实战化增补(每章新增可直接动手的内容):**
- ✅ 01:CLI 上手 checklist(安装→登录→最小任务→恢复会话);Realtime API / Gemini Live 端到端语音新节;faster-whisper CPU 示例
- ✅ 02:MCP 四步实战(FastMCP + Inspector + claude mcp add + Windows 踩坑);MCP Registry;A2A 1.0 迁移
- ✅ 03:Google ADK、Claude Agent SDK 入对比;各框架"安装 + 已验证版本"行
- ✅ 04:五分钟 Hooks 实战(exit 2 阻断 + 验证步骤);Cursor MDC 完整示例;SessionStart/PreCompact 事件
- ✅ 05:完整可运行 Agent Loop 脚本;Durable Execution(Temporal)与 LangGraph interrupt HITL 新章;GitHub Actions cron UTC 提醒
- ✅ 06:Structured Output 三家示例;推理模型提示差异对照表;Extended Thinking;promptfoo 最小配置
- ✅ 07:Mem0/Letta/Zep 选型对比;LangGraph Store;Context Engineering;带记忆对话 Agent 端到端示例
- ✅ 08:零成本混合检索 RAG(BM25+Chroma+BGE,无需 API key);LightRAG;MinerU/Docling/ColPali;Qwen3-Embedding/Reranker;RAG 生产运维
- ✅ 09:推理模型与 test-time compute;Chat Template 实务;TRL SFT/DPO 最小实操
- ✅ 10:P/D 分离(llm-d/Dynamo/LMCache);vLLM V1;国内实践(hf-mirror/ModelScope/gated 401);故障 Runbook
- ✅ 11:GRPO/RLVR 与推理模型对齐;HLE/SimpleQA/AIME/SWE-bench Verified 新基准;《人工智能生成合成内容标识办法》;garak/PyRIT 可跑命令

**口径修正:**
- ✅ 术语速查表条目数按实际统计(21~50 条/章,合计 391),不再声称"每章 50 条"
- ✅ 总行数 ~19,000 → ~22,400(+2,200 行实战内容)
- ✅ 无法核实的精确版本号统一降级为"以官方 release 为准"

#### v2.0(2026-07 重构 + 深度迭代)

**重大调整:**
- ✅ 从 4 个文档(01-04)重构为 11 个文档(01-11)+ README
- ✅ 按知识领域分类:基础层(06/07/09)→ 核心层(02/03/04/05)→ 应用层(01/08/10/11)
- ✅ 原 MCP 协议内容 → 归入 `02 智能体通信协议`
- ✅ 原 CLI 工具内容 → 归入 `01 交互入口` + `04 能力约束体系`
- ✅ 原 Agent 内容 → 归入 `03 智能体主体` + `05 任务编排`
- ✅ 原词汇表知识点 → 打散归入对应大类的详细文档中
- ✅ 新增独立大类:RAG 知识库(08)、底层模型(09)、部署运维(10)、安全评估(11)

**深度迭代(2026-07):**
- ✅ 所有 11 个章节完成深度迭代,每个章节开头新增 50 个术语速查表
- ✅ 新增 200+ 图表/表格(架构图/流程图/对比表/决策树)
- ✅ 新增 100+ 代码示例(可运行)
- ✅ 新增 50+ 论文链接
- ✅ 新增官方文档链接(覆盖所有主流厂商和工具)
- ✅ README 重构:增加全局词汇索引(A-Z)、4 种学习路径、技术栈全景图、应用场景对照表、FAQ、学习心法
- ✅ 总行数从 ~5,000 行扩展到 ~19,000 行

#### v1.0(初始版本)

- 4 个文档:MCP / CLI / Agent / 词汇表
- 约 5,000 行

### 15.3 重构原因

原文档按 MCP / CLI / Agent 三大工具划分,但用户的知识体系是从底层模型到上层应用的完整 AI 技术栈。改为按 11 大类知识领域组织,更符合学习和查阅的逻辑。

### 15.4 后续规划

- [x] ~~增加 14 章:多模态 Agent~~(已完成,见 `14-多模态Agent.md`)
- [x] ~~增加 15 章:构建自己的Agent全流程~~(已完成,见 `15-构建自己的Agent全流程.md`)
- [ ] 增加更多视频教程链接
- [ ] 增加 English 版本

---

## 🎯 结语

这份知识体系覆盖了从 LLM 基础到 Agent 应用、从模型底座到部署运维、从提示工程到安全评估的 AI 全栈知识。每个概念都附中英文对照 + 一句话解释,每个技术都有官方文档链接 + 代码示例。

**学习建议:** 不要追求一次性读完所有内容。按你的角色和目标,选择对应的学习路径,边学边做项目。遇到问题再回查具体章节。

> **"Theory without practice is empty; practice without theory is blind."**
> 理论没有实践是空洞的;实践没有理论是盲目的。—— 康德

---

**📌 反馈与改进:** 如发现错误、过时内容或建议新增,请直接修改对应章节的 Markdown 文件。

**📅 最后更新:** 2026-07-22
**📊 文档版本:** v4.3
**👤 维护者:** 学习者本人
