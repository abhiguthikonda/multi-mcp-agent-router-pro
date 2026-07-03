from openai import AsyncOpenAI

from config.settings import settings
from providers.base import BaseLLMProvider


class OpenRouterProvider(BaseLLMProvider):
    """
    OpenRouter implementation.

    OpenRouter exposes an OpenAI-compatible API, so we use the official
    OpenAI SDK with a custom base_url.
    """

    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
        )

    @property
    def provider_name(self) -> str:
        return "OpenRouter"

    async def generate(
        self,
        system_prompt: str,
        messages: list,
        tools: list | None = None,
        model: str = "deepseek/deepseek-r1-0528:free",
    ):
        """
        Generate a chat completion.
        """

        request_messages = [
            {
                "role": "system",
                "content": system_prompt,
            },
            *messages,
        ]

        response = await self.client.chat.completions.create(
            model=model,
            messages=request_messages,
            tools=tools,
        )

        return response