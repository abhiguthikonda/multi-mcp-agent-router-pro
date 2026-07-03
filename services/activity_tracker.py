from datetime import datetime

from core.events import ActivityEvent, EventType


class ActivityTracker:
    """
    Tracks everything the agent is doing.
    """

    def __init__(self):
        self.events: list[ActivityEvent] = []

    def add(
        self,
        title: str,
        description: str,
        event_type: EventType = EventType.INFO,
    ):
        self.events.append(
            ActivityEvent(
                timestamp=datetime.now(),
                title=title,
                description=description,
                event_type=event_type,
            )
        )

    def clear(self):
        self.events.clear()

    def get_events(self):
        return self.events