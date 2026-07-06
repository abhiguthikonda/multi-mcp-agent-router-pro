import streamlit as st


def render_message(role, content, agent="Assistant"):

    if role == "user":

        with st.chat_message("user"):
            st.markdown(content)

    else:

        with st.chat_message("assistant"):

            st.markdown(f"### 🤖 {agent}")

            st.markdown(content)