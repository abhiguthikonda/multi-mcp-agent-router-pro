from pathlib import Path
import shutil
from datetime import datetime


class UploadManager:
    """
    Handles saving uploaded files into the workspace/uploads directory.
    """

    def __init__(self):
        self.upload_dir = Path("workspace/uploads")
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    def save(self, uploaded_file):
        """
        Save uploaded file and return its metadata.
        """

        filename = uploaded_file.name
        destination = self.upload_dir / filename

        # Prevent overwriting existing files
        if destination.exists():

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            destination = (
                self.upload_dir
                / f"{timestamp}_{filename}"
            )

        with open(destination, "wb") as f:
            shutil.copyfileobj(uploaded_file, f)

        return {
            "name": destination.name,
            "path": str(destination),
            "size": destination.stat().st_size,
            "extension": destination.suffix.lower(),
            "uploaded_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        }

    def list_files(self):
        """
        Return all uploaded files.
        """

        files = []

        for file in self.upload_dir.iterdir():

            if file.is_file():

                files.append(
                    {
                        "name": file.name,
                        "path": str(file),
                        "size": file.stat().st_size,
                        "extension": file.suffix.lower(),
                    }
                )

        return files

    def delete(self, filename):
        """
        Delete a file from workspace/uploads.
        """

        target = self.upload_dir / filename

        if target.exists():
            target.unlink()
            return True

        return False

    def clear(self):
        """
        Delete all uploaded files.
        """

        for file in self.upload_dir.iterdir():

            if file.is_file():
                file.unlink()