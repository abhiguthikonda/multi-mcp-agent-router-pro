from dataclasses import dataclass, field


@dataclass
class BaseAgent:
    """
    Base definition for every specialized AI agent.
    """

    id: str
    name: str
    description: str
    system_prompt: str

    icon: str = "🤖"

    mcp_servers: list = field(default_factory=list)

    def supports_tools(self) -> bool:
        """Return True if this agent has MCP tools."""
        return bool(self.mcp_servers)