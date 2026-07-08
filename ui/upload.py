import streamlit as st

from services.upload_manager import UploadManager
from services.file_parser import FileParser


def render_upload():
    """
    Drag & Drop Upload Panel
    """

    st.subheader("📎 Upload Files")

    uploaded_files = st.file_uploader(
        "Drag & Drop files here or click to browse",
        type=[
            "pdf",
            "docx",
            "txt",
            "csv",
            "png",
            "jpg",
            "jpeg",
        ],
        accept_multiple_files=True,
    )

    if not uploaded_files:
        return

    manager = UploadManager()

    saved_files = []

    for uploaded_file in uploaded_files:

        file_info = manager.save(uploaded_file)

        parsed = FileParser.parse(file_info)

        file_info["parsed"] = parsed

        saved_files.append(file_info)

    # Add uploaded files into DocumentManager
    if "documents" in st.session_state:

        existing = {
            doc["name"]
            for doc in st.session_state.documents.get_all()
        }

        for file in saved_files:

            if file["name"] not in existing:
                st.session_state.documents.add(file)

    st.success(
        f"✅ Uploaded {len(saved_files)} file(s)"
    )

    st.divider()

    st.subheader("📂 Uploaded Files")

    for file in saved_files:

        parsed = file.get("parsed")

        icon = "📄"

        if parsed:

            if parsed["type"] == "image":
                icon = "🖼️"

            elif parsed["type"] == "csv":
                icon = "📊"

        st.write(
            f"{icon} **{file['name']}** ({round(file['size']/1024,2)} KB)"
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
                parsed["dataframe"].head(),
                use_container_width=True,
            )

        else:

            with st.expander(
                f"Preview - {file['name']}"
            ):

                st.text(
                    parsed["content"][:1000]
                )