"""模型接入层:OpenAI 兼容协议,一个工厂函数换任意端点。

对应第 15 章第五节"统一模型抽象层":换模型只改环境变量
(OPENAI_API_KEY / OPENAI_BASE_URL / MODEL_NAME),代码不动。
可接本地 vLLM / Ollama 的 OpenAI 兼容端点,或任意厂商接口。
"""
from __future__ import annotations

from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI

from .config import ModelSettings


def create_chat_model(settings: ModelSettings | None = None) -> BaseChatModel:
    """创建 OpenAI 兼容的 Chat 模型。配置缺失时抛出可读错误。"""
    settings = settings or ModelSettings()
    settings.validate()
    return ChatOpenAI(
        model=settings.model,
        base_url=settings.base_url or None,   # 空则走 OpenAI 官方默认
        api_key=settings.api_key,
        timeout=settings.timeout,
        max_retries=settings.max_retries,     # 5.5 节:重试/超时
    )
