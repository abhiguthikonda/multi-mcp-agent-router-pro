from datetime import datetime


class ActivityTracker:
    """
    Tracks execution activities during a request.
    """

    def __init__(self):
        self.activities = []

    def clear(self):
        self.activities.clear()

    def add(self, title, description=""):
        self.activities.append(
            {
                "time": datetime.now().strftime("%H:%M:%S"),
                "title": title,
                "description": description,
            }
        )

    def get_all(self):
        return self.activities