import asyncio

import streamlit as st

from core.agent_manager import AgentManager
from core.models import ChatRequest

from services.document_manager import DocumentManager

from ui.activity import render_activity
from ui.chat import render_chat
from ui.sidebar import render_sidebar
from ui.styles import load_styles
from ui.tool_history import render_tool_history
from ui.upload import render_upload
from ui.workspace import render_workspace

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

if "documents" not in st.session_state:
    st.session_state.documents = DocumentManager()

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

if "urls" not in st.session_state:
    st.session_state.urls = []

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
    "Multi-Agent AI Workspace powered by OpenRouter and MCP"
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
        len(st.session_state.messages),
    )

st.divider()

render_upload()

st.divider()

# -----------------------------
# Activity Timeline
# -----------------------------
with st.expander("🛠 Tool Execution", expanded=True):
    render_tool_history(manager.tool_executor)

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

    context = st.session_state.documents.build_context()

#temporarily added to show the context length for debugging purposes
    st.write("Document Context Length:", len(context))

    try:
        chat_response = asyncio.run(
            manager.chat(
                ChatRequest(
                    message=prompt,
                    provider=settings["provider"].lower(),
                    auto_route=settings["auto_route"],
                    selected_agent=settings["agent"],
                    uploaded_context=context,
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

    except Exception as e:
        st.error(str(e))
        st.stop()

    st.rerun()

st.divider()

render_workspace()