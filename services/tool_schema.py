"""
Convert MCP tools into OpenAI/OpenRouter tool definitions.
"""


def mcp_tool_to_openai(tool):

    return {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description or "",
            "parameters": tool.inputSchema,
        },
    }