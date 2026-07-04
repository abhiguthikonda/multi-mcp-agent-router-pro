import asyncio

from services.mcp_manager import MCPManager


async def main():

    manager = MCPManager()

    await manager.connect_filesystem()

    tools = await manager.get_openai_tools()

    print()

    print("First Tool")

    print(tools[0])

    await manager.disconnect()


asyncio.run(main())