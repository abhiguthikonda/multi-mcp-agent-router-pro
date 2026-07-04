from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    """
    Base interface for every LLM provider.
    """

    @property
    @abstractmethod
    def provider_name(self) -> str:
        pass

    @abstractmethod
    async def generate(
        self,
        system_prompt: str,
        messages: list,
        tools: list | None = None,
        model: str | None = None,
    ):
        """
        Generate a normal response.
        """
        pass

    @abstractmethod
    async def generate_with_tools(
        self,
        system_prompt: str,
        messages: list,
        tools: list,
        tool_executor,
        model: str | None = None,
    ):
        """
        Generate a response with automatic tool execution.
        """
        pass