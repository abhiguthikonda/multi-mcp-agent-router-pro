from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class EventType(str, Enum):
    INFO = "INFO"
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    ERROR = "ERROR"


@dataclass
class ActivityEvent:
    """
    Represents one event in the agent execution timeline.
    """

    timestamp: datetime
    title: str
    description: str
    event_type: EventType = EventType.INFO