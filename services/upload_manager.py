from pathlib import Path
import shutil


class UploadManager:
    """
    Handles saving uploaded files into workspace/uploads
    """

    def __init__(self):
        self.upload_dir = Path("workspace/uploads")
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    def save(self, uploaded_file):

        destination = self.upload_dir / uploaded_file.name

        with open(destination, "wb") as f:
            shutil.copyfileobj(uploaded_file, f)

        return {
            "name": uploaded_file.name,
            "path": str(destination),
            "size": destination.stat().st_size,
            "extension": destination.suffix.lower(),
        }