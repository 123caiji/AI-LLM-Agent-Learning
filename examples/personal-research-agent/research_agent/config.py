"""配置:环境变量 + CLI 参数汇聚一处。

模型接入走 OpenAI 兼容协议(对应第 15 章第五节"统一模型抽象层"):
    OPENAI_API_KEY   API 密钥(本地 vLLM/Ollama 可填任意非空串)
    OPENAI_BASE_URL  兼容端点,如 http://127.0.0.1:8000/v1
    MODEL_NAME       模型名
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

# 默认笔记目录:本包位于 <repo>/examples/personal-research-agent/research_agent/,
# parents[3] 即仓库根目录——直接用全书 15 个章节 .md 当默认笔记库。
DEFAULT_NOTES_DIR = Path(__file__).resolve().parents[3]
DEFAULT_WORKSPACE = Path(__file__).resolve().parents[2] / "agent_workspace"

ENV_API_KEY = "OPENAI_API_KEY"
ENV_BASE_URL = "OPENAI_BASE_URL"
ENV_MODEL_NAME = "MODEL_NAME"


@dataclass
class AgentConfig:
    """Agent 运行配置(与模型端点无关的部分)。"""

    notes_dir: Path = DEFAULT_NOTES_DIR
    workspace: Path = DEFAULT_WORKSPACE
    hitl: bool = True                # write_file 是否需要人工审批门(11.2 节)
    max_steps: int = 25              # 防止空转(9.1 节 MAX_STEPS)
    max_results: int = 5             # web_search 默认结果条数上限
    top_k: int = 5                   # search_notes 默认返回片段数
    audit_log: Path | None = None    # 审计日志,默认 <workspace>/.agent_audit.jsonl

    def __post_init__(self) -> None:
        self.notes_dir = Path(self.notes_dir).resolve()
        self.workspace = Path(self.workspace).resolve()
        if self.audit_log is None:
            self.audit_log = self.workspace / ".agent_audit.jsonl"


@dataclass
class ModelSettings:
    """模型端点配置(换模型只改这里 / 环境变量,第五节)。"""

    api_key: str = field(default_factory=lambda: os.environ.get(ENV_API_KEY, ""))
    base_url: str = field(default_factory=lambda: os.environ.get(ENV_BASE_URL, ""))
    model: str = field(default_factory=lambda: os.environ.get(ENV_MODEL_NAME, ""))
    timeout: int = 60
    max_retries: int = 2

    def validate(self) -> None:
        missing = [
            name
            for name, val in (
                (ENV_API_KEY, self.api_key),
                (ENV_BASE_URL, self.base_url),
                (ENV_MODEL_NAME, self.model),
            )
            if not val
        ]
        if missing:
            raise RuntimeError(
                f"缺少模型端点配置: {', '.join(missing)}。"
                "请设置环境变量,或复制 .env.example 为 .env 后填入。"
            )
