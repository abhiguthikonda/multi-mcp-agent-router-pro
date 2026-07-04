import streamlit as st

from ui.message import render_message


def render_chat():

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:

        render_message(
            message["role"],
            message["content"],
            message.get("agent", "Assistant"),
        )

    return st.chat_input("Ask anything...")