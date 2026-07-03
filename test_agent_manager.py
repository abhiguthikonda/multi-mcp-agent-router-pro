import asyncio

from core.agent_manager import AgentManager
from core.models import ChatRequest


async def main():

    manager = AgentManager()

    response = await manager.chat(
        ChatRequest(
            message="Explain Python decorators.",
            provider="openrouter",
        )
    )

    print()

    print("Agent :", response.agent_name)

    print("Provider :", response.provider)

    print("Response :", response.response)


asyncio.run(main())