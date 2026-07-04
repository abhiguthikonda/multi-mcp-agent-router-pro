
import asyncio

import streamlit as st

from ui.sidebar import render_sidebar
from ui.chat import render_chat

from core.agent_manager import AgentManager
from core.models import ChatRequest

try:
    from ui.styles import load_styles
except ImportError:
    def load_styles():
        pass

st.set_page_config(
    page_title="Multi MCP Agent Router Pro",
    page_icon="🤖",
    layout="wide",
)
load_styles()

# Sidebar
settings = render_sidebar()
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Keep one AgentManager instance
if "manager" not in st.session_state:
    st.session_state.manager = AgentManager()

manager = st.session_state.manager

# Title
st.title("🤖 Multi MCP Agent Router Pro")

st.caption(
    "Production-ready Multi-Agent AI using MCP"
)

# Chat UI
prompt = render_chat()

if prompt:

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