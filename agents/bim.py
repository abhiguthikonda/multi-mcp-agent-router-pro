from agents.base import BaseAgent


class BIMAgent(BaseAgent):
    """
    Specialized Building Information Modeling agent.
    """

    def __init__(self):
        super().__init__(
            id="bim",
            name="BIM Engineer",
            description="Assists with BIM, Revit and construction workflows.",
            icon="🏗️",
            system_prompt=(
                "You are an expert BIM engineer specializing in "
                "Autodesk Revit and construction documentation."
            ),
            mcp_servers=[
                {
                    "name": "filesystem",
                    "command": "npx",
                    "args": [
                        "-y",
                        "@modelcontextprotocol/server-filesystem",
                        "./workspace",
                    ],
                }
            ],
        )