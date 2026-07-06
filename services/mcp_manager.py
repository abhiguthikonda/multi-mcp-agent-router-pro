from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from config.settings import settings


class MCPManager:
    """
    Manages multiple MCP server connections.
    """

    def __init__(self):
        self.stack = None
        self.sessions = {}
        self.tool_to_server = {}
        self.connected = False

    # ==========================================================
    # Connection Lifecycle
    # ==========================================================

    async def connect(self):
        """
        Create a fresh AsyncExitStack.
        """

        if self.connected:
            return

        self.stack = AsyncExitStack()

        await self.stack.__aenter__()

        self.sessions.clear()

        self.tool_to_server.clear()

        self.connected = True

    async def disconnect(self):
        """
        Disconnect every MCP server.
        """

        if self.stack is not None:

            await self.stack.aclose()

        self.stack = None

        self.sessions.clear()

        self.tool_to_server.clear()

        self.connected = False

    # ==========================================================
    # Generic Server Connection
    # ==========================================================

    async def connect_server(
        self,
        server_name,
        command,
        args,
        env=None,
    ):
        """
        Connect any MCP server.
        """

        if not self.connected:
            await self.connect()

        params = StdioServerParameters(
            command=command,
            args=args,
            env=env,
        )

        transport = await self.stack.enter_async_context(
            stdio_client(params)
        )

        read_stream, write_stream = transport

        session = await self.stack.enter_async_context(
            ClientSession(
                read_stream,
                write_stream,
            )
        )

        await session.initialize()

        self.sessions[server_name] = session

# Automatically register every tool to its server
        result = await session.list_tools()
        for tool in result.tools:
            self.tool_to_server[tool.name] = server_name

    # ==========================================================
    # Filesystem MCP
    # ==========================================================

    async def connect_filesystem(self, directory="."):
        """
        Connect to the Filesystem MCP server.
        """

        await self.connect_server(
            server_name="filesystem",
            command="npx",
            args=[
                "-y",
                "@modelcontextprotocol/server-filesystem",
                directory,
            ],
        )

    # ==========================================================
    # GitHub MCP
    # ==========================================================

    async def connect_github(self):
        """
        Connect to the GitHub MCP server.
        """

        await self.connect_server(
            server_name="github",
            command="npx",
            args=[
                "-y",
                "@modelcontextprotocol/server-github",
            ],
            env={
                "GITHUB_PERSONAL_ACCESS_TOKEN": settings.GITHUB_TOKEN,
            },
        )


    # ==========================================================
    # Connect Everything
    # ==========================================================

    async def connect_all(self):
        """
        Connect all configured MCP servers.
        """

        if self.connected:
            return

        await self.connect()

        await self.connect_filesystem()

        await self.connect_github()
    # ==========================================================
    # Tool Discovery
    # ==========================================================

    async def list_tools(self):
        """
        Return every tool from every connected server.
        """

        if not self.connected:
            raise RuntimeError(
                "MCP Manager is not connected."
        )
        all_tools = []

        for session in self.sessions.values():
            result = await session.list_tools()
            all_tools.extend(result.tools)

        return all_tools

    # ==========================================================
    # Tool Execution
    # ==========================================================

    async def call_tool(
        self,
        tool_name,
        arguments,
    ):
        """
        Execute a tool on the correct server.
        """

        if not self.connected:
            raise RuntimeError(
                "MCP Manager is not connected."
            )

        if tool_name not in self.tool_to_server:
            raise RuntimeError(
                f"Unknown tool: {tool_name}"
            )

        server = self.tool_to_server[
            tool_name
        ]

        session = self.sessions[
            server
        ]

        return await session.call_tool(
            tool_name,
            arguments,
        )

    # ==========================================================
    # OpenAI/OpenRouter Tool Schema
    # ==========================================================

    async def get_openai_tools(self):
        """
        Convert all MCP tools into OpenAI/OpenRouter tool schemas.
        """

        from services.tool_schema import mcp_tool_to_openai

        tools = await self.list_tools()

        return [
            mcp_tool_to_openai(tool)
            for tool in tools
        ]