import streamlit as st


def render_activity(activity):

    st.subheader("⚡ Live Execution Timeline")

    items = activity.get_all()

    if not items:
        st.info("Waiting for a request...")
        return

    for item in items:

        with st.container():

            st.caption(item["time"])

            st.success(item["title"])

            if item["description"]:
                st.write(item["description"])

            st.divider()