import asyncio

from services.mcp_manager import MCPManager
from services.tool_executor import ToolExecutor


async def main():

    manager = MCPManager()

    await manager.connect_filesystem()

    executor = ToolExecutor(manager)

    result = await executor.execute(
        "read_text_file",
        {
            "path": "README.md"
        },
    )

    print("\nREADME CONTENT\n")
    print("-" * 50)

    for content in result.content:
        print(content.text)

    await manager.disconnect()


asyncio.run(main())