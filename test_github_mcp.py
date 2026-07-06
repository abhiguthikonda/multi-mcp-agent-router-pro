import asyncio

from services.mcp_manager import MCPManager


async def main():

    manager = MCPManager()

    print("Connecting to GitHub MCP...")

    await manager.connect_github()

    print("Connected!")

    session = manager.sessions["github"]

    result = await session.list_tools()

    print("\nAvailable GitHub Tools")
    print("-" * 40)

    for tool in result.tools:
        print(tool.name)

    await manager.disconnect()


asyncio.run(main())