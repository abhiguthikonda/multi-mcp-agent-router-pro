import json


class ToolExecutor:
    """
    Executes tools exposed by MCP servers.
    """

    def __init__(self, manager):
        self.manager = manager

    async def execute(
        self,
        tool_name,
        arguments,
    ):
        """
        Execute an MCP tool directly.
        """
        return await self.manager.call_tool(
            tool_name,
            arguments,
        )

    async def execute_tool_call(
        self,
        tool_call,
    ):
        """
        Execute an OpenAI/OpenRouter tool call.
        """

        tool_name = tool_call.function.name

        arguments = json.loads(
            tool_call.function.arguments
        )

        result = await self.execute(
            tool_name,
            arguments,
        )

        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(result),
        }