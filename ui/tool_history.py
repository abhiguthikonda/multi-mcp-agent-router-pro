import streamlit as st


def render_tool_history(tool_executor):

    st.subheader("🛠 Tools Used")

    history = tool_executor.get_history()

    if not history:
        st.info("No tools executed.")
        return

    for tool in history:
        st.success(tool)