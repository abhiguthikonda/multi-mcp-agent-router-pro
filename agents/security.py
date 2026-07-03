from agents.base import BaseAgent


class SecurityAgent(BaseAgent):
    """
    Specialized cybersecurity agent.
    """

    def __init__(self):
        super().__init__(
            id="security",
            name="Security Auditor",
            description="Reviews applications for security vulnerabilities.",
            icon="🛡️",
            system_prompt=(
                "You are an application security expert.\n"
                "Check for:\n"
                "- OWASP Top 10\n"
                "- Secrets\n"
                "- Injection\n"
                "- Authentication flaws\n"
                "- Authorization issues"
            ),
            mcp_servers=[
                {
                    "name": "github",
                    "command": "npx",
                    "args": [
                        "-y",
                        "@modelcontextprotocol/server-github",
                    ],
                },
                {
                    "name": "fetch",
                    "command": "npx",
                    "args": [
                        "-y",
                        "@modelcontextprotocol/server-fetch",
                    ],
                },
            ],
        )