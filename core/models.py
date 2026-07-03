from dataclasses import dataclass


@dataclass
class ChatRequest:
    """
    User chat request.
    """

    message: str

    provider: str = "openrouter"

    auto_route: bool = True

    selected_agent: str | None = None


@dataclass
class ChatResponse:
    """
    Response returned by the AgentManager.
    """

    agent_id: str

    agent_name: str

    provider: str

    response: str