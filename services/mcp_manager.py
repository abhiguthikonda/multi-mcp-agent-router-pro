from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class MCPManager:
    """
    Manages MCP server connections.
    """

    def __init__(self):
        self.stack = None
        self.session = None
        self.connected = False

    async def connect_filesystem(self, directory="."):
        """
        Connect to the Filesystem MCP server.
        """

        # Always create a fresh AsyncExitStack
        self.stack = AsyncExitStack()

        await self.stack.__aenter__()

        params = StdioServerParameters(
            command="npx",
            args=[
                "-y",
                "@modelcontextprotocol/server-filesystem",
                directory,
            ],
        )

        transport = await self.stack.enter_async_context(
            stdio_client(params)
        )

        read_stream, write_stream = transport

        self.session = await self.stack.enter_async_context(
            ClientSession(read_stream, write_stream)
        )

        await self.session.initialize()

        self.connected = True

    async def disconnect(self):
        """
        Disconnect from the MCP server.
        """

        if self.stack is not None:

            await self.stack.aclose()

            self.stack = None
            self.session = None
            self.connected = False

    async def list_tools(self):

        if not self.connected:
            raise RuntimeError(
                "No MCP server connected."
            )

        result = await self.session.list_tools()

        return result.tools

    async def call_tool(
        self,
        tool_name,
        arguments,
    ):

        if not self.connected:
            raise RuntimeError(
                "No MCP server connected."
            )

        return await self.session.call_tool(
            tool_name,
            arguments,
        )

    async def get_openai_tools(self):

        from services.tool_schema import mcp_tool_to_openai

        tools = await self.list_tools()

        return [
            mcp_tool_to_openai(tool)
            for tool in tools
        ]