import asyncio

import streamlit as st

from ui.sidebar import render_sidebar
from ui.chat import render_chat
from ui.activity import render_activity
from ui.styles import load_styles
from ui.tool_history import render_tool_history
from core.agent_manager import AgentManager
from core.models import ChatRequest


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Multi MCP Agent Router Pro",
    page_icon="🤖",
    layout="wide",
)

load_styles()


# -----------------------------
# Session State Initialization
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "manager" not in st.session_state:
    st.session_state.manager = AgentManager()

manager = st.session_state.manager


# -----------------------------
# Sidebar
# -----------------------------
settings = render_sidebar()



# -----------------------------
# Header
# -----------------------------
st.title("🤖 Multi MCP Agent Router Pro")

st.caption(
    "Production-ready Multi-Agent AI using MCP"
)


# -----------------------------
# Dashboard Metrics
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Connected MCP Servers",
        len(manager.mcp.sessions),
    )

with col2:
    st.metric(
        "Messages",
        len(st.session_state.get("messages", [])),
    )


st.divider()
with st.expander("🛠 Tool Execution", expanded=True):
    render_tool_history(manager.tool_executor)


# -----------------------------
# Activity Timeline
# -----------------------------
with st.expander("⚡ Activity Timeline", expanded=True):
    render_activity(manager.activity)


st.divider()


# -----------------------------
# Chat
# -----------------------------
prompt = render_chat()


# -----------------------------
# Handle Prompt
# -----------------------------
if prompt:
    manager.tool_executor.clear_history()

    chat_response = asyncio.run(
        manager.chat(
            ChatRequest(
                message=prompt,
                provider=settings["provider"].lower(),
                auto_route=settings["auto_route"],
                selected_agent=settings["agent"],
            )
        )
    )

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": chat_response.response,
            "agent": chat_response.agent_name,
        }
    )

    st.rerun()