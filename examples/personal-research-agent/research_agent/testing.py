"""离线测试用假模型:按预设脚本依次返回消息,不需要任何 API key。

供 tests/test_smoke.py 与 evals/run_eval.py --offline 使用。
做法与 langchain_core 的 FakeListChatModel 同思路,但额外支持
tool_calls 脚本化(FakeListChatModel 只能回纯文本,没法测工具循环)。
"""
from __future__ import annotations

from typing import Any

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, BaseMessage
from langchain_core.outputs import ChatGeneration, ChatResult


class ScriptedChatModel(BaseChatModel):
    """按 script 队列逐条返回 AIMessage;队列耗尽后回兜底文本。"""

    script: list[AIMessage]
    calls: list[list[BaseMessage]] = []  # 记录每轮收到的消息,便于断言

    @property
    def _llm_type(self) -> str:
        return "scripted-fake"

    def bind_tools(self, tools: Any, **kwargs: Any) -> "ScriptedChatModel":
        # 假模型不需要真的绑 schema,记录下来即可
        self._bound_tools = list(tools)
        return self

    def _generate(
        self,
        messages: list[BaseMessage],
        stop: list[str] | None = None,
        run_manager: Any = None,
        **kwargs: Any,
    ) -> ChatResult:
        self.calls.append(list(messages))
        if self.script:
            msg = self.script.pop(0)
        else:
            msg = AIMessage(content="(脚本耗尽,兜底回复)")
        return ChatResult(generations=[ChatGeneration(message=msg)])


def tool_call_msg(name: str, args: dict, call_id: str = "call_1") -> AIMessage:
    """构造一条带工具调用的 AIMessage(脚本原料)。"""
    return AIMessage(
        content="", tool_calls=[{"name": name, "args": args, "id": call_id}]
    )
