from agents import registry
from core.models import ChatRequest, ChatResponse
from core.context import ExecutionContext
from routers.keyword_router import KeywordRouter

from providers.factory import get_provider
from services.activity_tracker import ActivityTracker
from services.memory import MemoryManager
from services.logger import logger


class AgentManager:
    """
    Central orchestrator for the Multi MCP Agent Router.
    """

    def __init__(self):
        self.activity = ActivityTracker()
        self.router = KeywordRouter()
        self.memory = MemoryManager()

    async def chat(self, request: ChatRequest) -> ChatResponse:
        """
        Process a chat request.
        """

        self.activity.clear()

        logger.info("Received user query.")

        self.activity.add(
            "Query Received",
            request.message,
        )

        context = ExecutionContext(request)

        if request.auto_route:
            agent = self.router.route(request.message)
        else:
            agent = registry.get(request.selected_agent)

        context.selected_agent = agent.id

        logger.info(f"Selected agent: {agent.name}")

        self.activity.add(
            "Agent Selected",
            agent.name,
        )

        self.memory.add_message(
            agent.id,
            "user",
            request.message,
        )

        self.memory.add_message(
            agent.id,
            "assistant",
            "This is a placeholder response from AgentManager.",
        )

        provider = get_provider(request.provider)

        logger.info(f"Selected provider: {provider.provider_name}")

        self.activity.add(
              "Provider Selected",
               provider.provider_name,
        )

        return ChatResponse(
            agent_id=context.selected_agent,
            agent_name=agent.name,
            provider=provider.provider_name,
            response="This is a placeholder response from AgentManager.",
        )