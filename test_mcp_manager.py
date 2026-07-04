import asyncio

from services.mcp_manager import MCPManager


async def main():

    manager = MCPManager()

    print("Connecting...")

    await manager.connect_filesystem()

    print("Connected!")

    tools = await manager.list_tools()

    print()

    print("Available Tools")

    print("-" * 40)

    for tool in tools:

        print(tool.name)

    await manager.disconnect()

    print()

    print("Disconnected!")


asyncio.run(main())