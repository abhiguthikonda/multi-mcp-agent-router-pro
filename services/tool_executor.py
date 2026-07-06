import json


class ToolExecutor:
    """
    Executes tools exposed by MCP servers and records execution history.
    """

    def __init__(self, manager):
        self.manager = manager
        self.executed_tools = []

    def clear_history(self):
        self.executed_tools.clear()

    def get_history(self):
        return self.executed_tools

    async def execute(
        self,
        tool_name,
        arguments,
    ):
        """
        Execute an MCP tool directly.
        """

        self.executed_tools.append(tool_name)

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