from agents.base import BaseAgent


class CodeReviewerAgent(BaseAgent):
    """
    Specialized agent for reviewing source code.
    """

    def __init__(self):
        super().__init__(
            id="code_reviewer",
            name="Code Reviewer",
            description="Reviews code quality, bugs, performance and maintainability.",
            icon="🔍",
            system_prompt=(
                "You are an expert software engineer and code reviewer.\n"
                "Review code for:\n"
                "- Bugs\n"
                "- Logic errors\n"
                "- Code smells\n"
                "- Performance issues\n"
                "- Security vulnerabilities\n"
                "- Best practices\n\n"
                "Always explain WHY something should be changed."
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
                    "name": "filesystem",
                    "command": "npx",
                    "args": [
                        "-y",
                        "@modelcontextprotocol/server-filesystem",
                        "./workspace",
                    ],
                },
            ],
        )