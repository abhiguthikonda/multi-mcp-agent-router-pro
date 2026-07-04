import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    params = StdioServerParameters(
        command="npx",
        args=[
            "-y",
            "@modelcontextprotocol/server-filesystem",
            ".",
        ],
    )

    async with stdio_client(params) as (read, write):

        async with ClientSession(read, write) as session:

            print("\nConnecting to MCP Server...")

            await session.initialize()

            print("Connected!")

            result = await session.list_tools()

            print("\nAvailable Tools")
            print("-" * 40)

            for tool in result.tools:
                print(f"• {tool.name}")
                print(f"  {tool.description}\n")


if __name__ == "__main__":
    asyncio.run(main())