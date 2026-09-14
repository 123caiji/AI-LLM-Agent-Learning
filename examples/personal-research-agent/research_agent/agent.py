"""Agent 图编排:LangGraph 版 ReAct 循环 + checkpoint + 人工审批门。

对应第 15 章 9.2 节"LangGraph 版:图编排 + 状态持久化":

    节点: agent(调用LLM) → tools(执行工具) → agent → ... → END
    边:   条件路由 "还有工具调用?" → 是→tools 否→END

在此基础上落实 11.2 节的两件事:
- write_file(L1 可逆写)执行前 interrupt() 挂起,等人工确认(审批门);
- 每笔工具调用写审计日志(JSONL)。
"""
from __future__ import annotations

import json
from typing import Annotated, Literal, TypedDict

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, BaseMessage, ToolMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages
from langgraph.types import interrupt

from .config import AgentConfig
from .prompts import SYSTEM_PROMPT
from .security import audit
from .tools import make_tools

# 需要人工审批的工具(11.2 节:L1 可逆写也要审批门,防模型乱写)
HITL_TOOLS = {"write_file"}
# 工具结果回灌上下文前的裁剪上限(第五节)
MAX_RESULT_CHARS = 2000


class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]  # 自动合并而非覆盖
    step_count: int


def build_graph(
    model: BaseChatModel,
    config: AgentConfig,
    checkpointer=None,
):
    """构建并编译 Agent 图。

    model: 任意 BaseChatModel(生产用 OpenAI 兼容模型,测试用假模型)。
    checkpointer: 默认 MemorySaver;传 SqliteSaver 可跨进程持久化。
    """
    tools = make_tools(config)
    tools_by_name = {t.name: t for t in tools}
    model_with_tools = model.bind_tools(tools)

    # ---- 节点 1: 调用 LLM ----
    def call_model(state: State) -> dict:
        response = model_with_tools.invoke(state["messages"])
        return {"messages": [response], "step_count": state["step_count"] + 1}

    # ---- 节点 2: 执行工具(含审批门 + 审计) ----
    def execute_tools(state: State) -> dict:
        last = state["messages"][-1]
        assert isinstance(last, AIMessage) and last.tool_calls
        results: list[ToolMessage] = []
        for tc in last.tool_calls:
            name, args, call_id = tc["name"], tc["args"], tc["id"]

            # 人工审批门(11.2 节 LangGraph interrupt 写法)
            if config.hitl and name in HITL_TOOLS:
                approval = interrupt({"action": name, "args": args})
                approved = isinstance(approval, dict) and approval.get("approved")
                audit(config.audit_log, {
                    "event": "hitl", "tool": name,
                    "args_summary": str(args)[:200], "approved": bool(approved),
                })
                if not approved:
                    results.append(ToolMessage(
                        content="用户拒绝了此写入操作,文件未修改。请改用其他方式回应用户。",
                        tool_call_id=call_id,
                    ))
                    continue

            tool = tools_by_name.get(name)
            if tool is None:
                output = json.dumps({"error": f"未知工具 {name!r}"}, ensure_ascii=False)
            else:
                try:
                    output = str(tool.invoke(args))
                except Exception as e:  # 错误可消化(6.1 节)
                    output = json.dumps(
                        {"error": f"工具 {name} 执行失败: {e}"}, ensure_ascii=False
                    )
            audit(config.audit_log, {
                "event": "tool_call", "tool": name,
                "args_summary": str(args)[:200], "result_summary": output[:200],
            })
            results.append(ToolMessage(
                content=output[:MAX_RESULT_CHARS], tool_call_id=call_id
            ))
        return {"messages": results}

    # ---- 条件路由:判断下一步 ----
    def should_continue(state: State) -> Literal["tools", "__end__"]:
        last = state["messages"][-1]
        if state["step_count"] >= config.max_steps:
            return END
        if isinstance(last, AIMessage) and last.tool_calls:
            return "tools"
        return END

    # ---- 构建图 ----
    builder = StateGraph(State)
    builder.add_node("agent", call_model)
    builder.add_node("tools", execute_tools)
    builder.set_entry_point("agent")
    builder.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})
    builder.add_edge("tools", "agent")

    return builder.compile(checkpointer=checkpointer or MemorySaver())


def initial_state(task: str) -> State:
    return {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": task},
        ],
        "step_count": 0,
    }
