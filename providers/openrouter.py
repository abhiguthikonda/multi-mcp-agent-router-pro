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
        model=None,
    ):
        """Generate a chat completion via OpenRouter/OpenAI AsyncOpenAI client."""

        
        client = self._get_client()
        model = model or settings.DEFAULT_MODEL

        request_messages = [
            {"role": "system", "content": system_prompt},
            *messages,
        ]

        response = await client.chat.completions.create(
            model=model,
            messages=request_messages,
            tools=tools,
            max_tokens=settings.MAX_TOKENS,
            temperature=0.2,
        )

        return response

    async def generate_with_tools(
        self,
        system_prompt,
        messages,
        tools,
        tool_executor,
        model=None,
    ):
        """
        Generate a response with OpenAI tool calling.
        """

        client = self._get_client()

        model = model or settings.DEFAULT_MODEL

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
            max_tokens=settings.MAX_TOKENS,
            temperature=0.2,
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return response

        request_messages.append(message)

        for tool_call in message.tool_calls:
            tool_result = await tool_executor.execute_tool_call(
                tool_call
            )

            request_messages.append(tool_result)

        final_response = await client.chat.completions.create(
            model=model,
            messages=request_messages,
            tools=tools,
            temperature=0.2,
            max_tokens=settings.MAX_TOKENS,
        )

        return final_response