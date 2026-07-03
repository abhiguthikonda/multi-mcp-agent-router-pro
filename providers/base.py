from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    """
    Base class for all LLM providers.

    Every provider (OpenRouter, Gemini, Ollama, Anthropic)
    must implement this interface.
    """

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Return provider name."""
        pass

    @abstractmethod
    async def generate(
        self,
        system_prompt: str,
        messages: list,
        tools: list | None = None,
    ):
        """
        Generate a response from the model.
        """
        pass