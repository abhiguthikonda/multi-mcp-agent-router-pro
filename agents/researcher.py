from agents.base import BaseAgent


class ResearchAgent(BaseAgent):
    """
    Specialized research assistant.
    """

    def __init__(self):
        super().__init__(
            id="researcher",
            name="Research Agent",
            description="Researches topics and summarizes information.",
            icon="📚",
            system_prompt=(
                "You are an expert research assistant.\n"
                "Provide factual, well-structured answers.\n"
                "Always cite reliable sources whenever possible."
            ),
            mcp_servers=[
                {
                    "name": "fetch",
                    "command": "npx",
                    "args": [
                        "-y",
                        "@modelcontextprotocol/server-fetch",
                    ],
                }
            ],
        )