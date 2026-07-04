import asyncio

from services.mcp_manager import MCPManager
from services.tool_executor import ToolExecutor


async def main():

    manager = MCPManager()

    await manager.connect_filesystem()

    executor = ToolExecutor(manager)

    result = await executor.execute(
        "list_allowed_directories",
        {},
    )

    print()

    print("Allowed Directories")

    print("-" * 40)

    for content in result.content:
        print(content.text)

    await manager.disconnect()


asyncio.run(main())