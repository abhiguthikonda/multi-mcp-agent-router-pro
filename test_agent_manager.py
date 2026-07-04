import asyncio

from core.agent_manager import AgentManager
from core.models import ChatRequest


async def main():

    manager = AgentManager()

    response = await manager.chat(
        ChatRequest(
            message="Explain Python decorators with an example.",
            provider="openrouter",
        )
    )

    print()

    print("Agent :", response.agent_name)

    print("Provider :", response.provider)

    print("Response :", response.response)

    print()

    print("Conversation History")

    for message in manager.memory.get_history(response.agent_id):
        print(message)


asyncio.run(main())