import streamlit as st


def render_workspace():
    """
    Displays uploaded documents.
    """

    st.subheader("📂 Workspace")

    if "documents" not in st.session_state:

        st.info("No uploaded files.")

        return

    documents = st.session_state.documents.get_all()

    if not documents:

        st.info("No uploaded files.")

        return

    for document in documents:

        parsed = document.get("parsed")

        icon = "📄"

        if parsed:

            if parsed["type"] == "csv":
                icon = "📊"

            elif parsed["type"] == "image":
                icon = "🖼️"

            elif parsed["type"] == "url":
                icon = "🌐"

        with st.expander(
            f"{icon} {document['name']}",
            expanded=False,
        ):

            st.write(
                f"**Size:** {round(document['size']/1024,2)} KB"
            )

            if not parsed:
                continue

            if parsed["type"] == "image":

                st.image(
                    parsed["image"],
                    use_container_width=True,
                )

            elif parsed["type"] == "csv":

                st.dataframe(
                    parsed["dataframe"],
                    use_container_width=True,
                )

            else:

                st.text(
                    parsed["content"][:1000]
                )