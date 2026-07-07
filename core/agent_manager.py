from asyncio import tools
from services.mcp_manager import MCPManager
from services.tool_executor import ToolExecutor

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

        self.mcp = MCPManager()

        self.tool_executor = ToolExecutor(
            self.mcp
        )

    async def chat(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
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

            agent = self.router.route(
                request.message
            )

        else:

            agent = registry.get(
                request.selected_agent
            )

        context.selected_agent = agent.id

        self.memory.add_message(
            agent.id,
            "user",
            request.message,
        )

        logger.info(
            f"Selected agent: {agent.name}"
        )

        self.activity.add(
            "Agent Selected",
            agent.name,
        )

        # Connect every MCP server
        await self.mcp.connect_all()
        self.activity.add(
            "Connected MCP Servers",
            ", ".join(self.mcp.sessions.keys()),
        )

        try:

            provider = get_provider(
                request.provider
            )

            logger.info(
                f"Selected provider: {provider.provider_name}"
            )

            self.activity.add(
                "Provider Selected",
                provider.provider_name,
            )

            tools = await self.mcp.get_openai_tools()
            self.activity.add(
                "Loaded MCP Tools",
                str(len(tools)),
            )

            self.activity.add(
                "LLM Thinking",
                provider.provider_name,
)
            print("Calling OpenRouter...")
            print("Tools:", len(tools))
            print("Messages:", len(self.memory.get_history(agent.id)))
            
            response = await provider.generate_with_tools(
                system_prompt=agent.system_prompt,
                messages=self.memory.get_history(
                    agent.id
                ),
                tools=tools,
                tool_executor=self.tool_executor,
            )

            assistant_message = (
                response.choices[0]
                .message.content
            )

            self.memory.add_message(
                agent.id,
                "assistant",
                assistant_message,
            )

            self.activity.add(
                "Response Generated",
                agent.name,
)
            return ChatResponse(
                agent_id=context.selected_agent,
                agent_name=agent.name,
                provider=provider.provider_name,
                response=assistant_message,
            )

        finally:

            await self.mcp.disconnect()