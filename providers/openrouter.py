from openai import AsyncOpenAI

from config.settings import settings
from providers.base import BaseLLMProvider


class OpenRouterProvider(BaseLLMProvider):
    """
    OpenRouter implementation using lazy initialization.
    """

    def __init__(self):
        self.client = None

    @property
    def provider_name(self):
        return "OpenRouter"

    def _get_client(self):
        """
        Create the OpenAI client only when needed.
        """

        if self.client is None:

            if not settings.OPENROUTER_API_KEY:
                raise ValueError(
                    "OPENROUTER_API_KEY is not configured."
                )

            self.client = AsyncOpenAI(
                api_key=settings.OPENROUTER_API_KEY,
                base_url="https://openrouter.ai/api/v1",
            )

        return self.client

    async def generate(
        self,
        system_prompt,
        messages,
        tools=None,
        model="deepseek/deepseek-r1-0528:free",
    ):

        client = self._get_client()

        request_messages = [
            {
                "role": "system",
                "content": system_prompt,
            },
            *messages,
        ]

        response = await client.chat.completions.create(
            model=model,
            messages=request_messages,
            tools=tools,
        )

        return response