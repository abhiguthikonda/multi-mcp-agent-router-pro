import streamlit as st


def render_sidebar():

    st.sidebar.title("⚙ Control Panel")

    provider = "OpenRouter"

    st.sidebar.markdown("### 🧠 Provider")
    st.sidebar.success("OpenRouter")

    auto_route = st.sidebar.checkbox(
        "Auto Route",
        value=True,
    )

    agent = st.sidebar.selectbox(
        "Agent",
        [
            "Research Agent",
            "Code Reviewer",
            "General Assistant",
        ],
    )

    st.sidebar.divider()

    st.sidebar.subheader("🟢 MCP Servers")

    manager = st.session_state.get("manager")

    if manager:

        filesystem = "filesystem" in manager.mcp.sessions
        github = "github" in manager.mcp.sessions

        st.sidebar.write(
            f"{'🟢' if filesystem else '🔴'} Filesystem"
        )

        st.sidebar.write(
            f"{'🟢' if github else '🔴'} GitHub"
        )

        st.sidebar.divider()

        st.sidebar.subheader("📊 Statistics")

        st.sidebar.metric(
            "Connected Servers",
            len(manager.mcp.sessions),
        )

        st.sidebar.metric(
            "Available Tools",
            len(manager.mcp.tool_to_server),
        )

        st.sidebar.metric(
            "Messages",
            len(st.session_state.get("messages", [])),
        )

    st.sidebar.divider()

    if st.sidebar.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    return {
        "provider": provider,
        "auto_route": auto_route,
        "agent": agent,
    }