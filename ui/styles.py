import streamlit as st


def load_styles():

    st.markdown(
        """
<style>

/* Main width */

.block-container{
    max-width:1200px;
    padding-top:20px;
}

/* Hide Streamlit menu/footer */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* User row */

.user-row{
    display:flex;
    justify-content:flex-end;
    margin:18px 0;
}

/* Assistant row */

.assistant-row{
    display:flex;
    justify-content:flex-start;
    margin:18px 0;
}

/* User Bubble */

.user-bubble{

    background:#2B7FFF;

    color:white;

    padding:14px 18px;

    border-radius:18px 18px 4px 18px;

    max-width:70%;

    font-size:16px;

    line-height:1.6;

    box-shadow:0 2px 8px rgba(0,0,0,.15);
}

/* Assistant Bubble */

.assistant-bubble{

    background:white;

    border:1px solid #E5E7EB;

    padding:14px 18px;

    border-radius:18px 18px 18px 4px;

    max-width:80%;

    font-size:16px;

    line-height:1.7;

    box-shadow:0 2px 10px rgba(0,0,0,.06);
}

/* Agent Name */

.agent-name{

    color:#666;

    font-size:13px;

    margin-bottom:6px;

    font-weight:600;
}

/* User Name */

.user-name{

    color:#666;

    font-size:13px;

    text-align:right;

    margin-bottom:6px;

    font-weight:600;
}

</style>
        """,
        unsafe_allow_html=True,
    )