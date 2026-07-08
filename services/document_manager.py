from typing import List


class DocumentManager:
    """
    Stores uploaded documents and builds context
    for the LLM.
    """

    def __init__(self):
        self.documents: List[dict] = []

    def add(self, file_info: dict):
        """
        Add uploaded file metadata.
        """
        self.documents.append(file_info)

    def get_all(self):
        """
        Return all uploaded documents.
        """
        return self.documents

    def clear(self):
        """
        Remove all uploaded documents.
        """
        self.documents.clear()

    def count(self):
        return len(self.documents)

    def build_context(self):
        """
        Convert uploaded files into LLM context.
        """

        if not self.documents:
            return ""

        context = ""

        for document in self.documents:

            parsed = document.get("parsed")

            if not parsed:
                continue

            context += "\n"
            context += "=" * 70
            context += "\n"

            context += f"Document: {document['name']}\n\n"

            if parsed["type"] in [
                "pdf",
                "docx",
                "txt",
                "url",
            ]:

                context += parsed["content"][:4000]

            elif parsed["type"] == "csv":

                context += (
                    parsed["dataframe"]
                    .head(20)
                    .to_string()
                )

            elif parsed["type"] == "image":

                context += (
                    "Image uploaded. "
                    "Visual analysis is not implemented yet."
                )

            context += "\n"

        return context