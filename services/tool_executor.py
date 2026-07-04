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
        return await self.manager.call_tool(
        tool_name,
        arguments,
        )