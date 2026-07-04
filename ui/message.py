import streamlit as st


def render_message(role, content, agent="Assistant"):

    if role == "user":

        st.markdown(
            f"""
<div class="user-row">

<div>

<div class="user-name">
👤 You
</div>

<div class="user-bubble">

{content}

</div>

</div>

</div>
""",
            unsafe_allow_html=True,
        )

    else:

        st.markdown(
            f"""
<div class="assistant-row">

<div>

<div class="agent-name">
🤖 {agent}
</div>

<div class="assistant-bubble">

{content}

</div>

</div>

</div>
""",
            unsafe_allow_html=True,
        )