from dataclasses import dataclass, field
from time import time

from core.events import ActivityEvent
from core.models import ChatRequest


@dataclass
class ExecutionContext:
    """
    Holds all information related to a single user request.
    Every service updates this object.
    """

    request: ChatRequest

    selected_agent: str | None = None

    provider: str | None = None

    messages: list = field(default_factory=list)

    tool_calls: list = field(default_factory=list)

    activity: list[ActivityEvent] = field(default_factory=list)

    response: str = ""

    start_time: float = field(default_factory=time)

    end_time: float = 0

    def execution_time(self) -> float:
        if self.end_time == 0:
            return 0
        return round(self.end_time - self.start_time, 2)