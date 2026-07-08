from pathlib import Path

import pandas as pd
import pdfplumber
from docx import Document
from PIL import Image


class FileParser:
    """
    Parses uploaded files into content usable by the AI.
    """

    @staticmethod
    def parse(file_info: dict):

        path = Path(file_info["path"])

        extension = path.suffix.lower()

        if extension == ".pdf":
            return FileParser.parse_pdf(path)

        elif extension == ".docx":
            return FileParser.parse_docx(path)

        elif extension == ".txt":
            return FileParser.parse_txt(path)

        elif extension == ".csv":
            return FileParser.parse_csv(path)

        elif extension in [
            ".png",
            ".jpg",
            ".jpeg",
        ]:
            return FileParser.parse_image(path)

        return None

    @staticmethod
    def parse_pdf(path):

        text = ""

        with pdfplumber.open(path) as pdf:

            for page in pdf.pages:

                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

        return {
            "type": "pdf",
            "content": text,
        }

    @staticmethod
    def parse_docx(path):

        doc = Document(path)

        text = "\n".join(
            p.text
            for p in doc.paragraphs
        )

        return {
            "type": "docx",
            "content": text,
        }

    @staticmethod
    def parse_txt(path):

        text = path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

        return {
            "type": "txt",
            "content": text,
        }

    @staticmethod
    def parse_csv(path):

        df = pd.read_csv(path)

        return {
            "type": "csv",
            "dataframe": df,
        }

    @staticmethod
    def parse_image(path):

        image = Image.open(path)

        return {
            "type": "image",
            "image": image,
        }