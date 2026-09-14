"""个人研究助手 Agent —— 《AI-LLM-Agent-Learning》第 15 章配套实战代码。

运行在本机,能检索本地 Markdown 笔记库、联网搜索、读写工作目录文件,
并按给定题目产出带引用的研究摘要。

对应书中章节:
- 第五节  模型接入层      -> research_agent/model.py
- 第六节  工具设计        -> research_agent/tools.py
- 第七节  System Prompt   -> research_agent/prompts.py
- 8.3     最小 RAG        -> research_agent/notes_index.py
- 9.2     LangGraph 版图编排 -> research_agent/agent.py
- 11.2    安全三层加固    -> research_agent/security.py + agent.py 审批门
"""

__version__ = "0.1.0"
