import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("⚙️ Settings")

        provider = st.selectbox(
            "Provider",
            [
                "OpenRouter",
            ],
        )

        auto_route = st.checkbox(
            "Auto Route",
            value=True,
        )

        agent = st.selectbox(
            "Agent",
            [
                "Research Agent",
                "Code Reviewer",
                "Security Auditor",
                "BIM Engineer",
            ],
        )

        return {
            "provider": provider,
            "auto_route": auto_route,
            "agent": agent,
        }