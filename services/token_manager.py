from typing import List


class TokenManager:
    """
    Controls how much context is sent to the LLM.
    """

    MAX_HISTORY = 6          # last 8 chat messages
    MAX_CONTEXT_CHARS = 2000 # uploaded document context
    MAX_TOOL_CHARS =   500    # tool outputs

    @staticmethod
    def trim_messages(messages: List[dict]) -> List[dict]:
        """
        Keep only the most recent chat messages.
        """
        if len(messages) <= TokenManager.MAX_HISTORY:
            return messages

        return messages[-TokenManager.MAX_HISTORY:]

    @staticmethod
    def trim_context(context: str) -> str:
        """
        Reduce uploaded context.
        """
        if not context:
            return ""

        return context[:TokenManager.MAX_CONTEXT_CHARS]

    @staticmethod
    def trim_tool_output(text: str) -> str:
        """
        Reduce tool outputs.
        """
        if not text:
            return ""

        return text[:TokenManager.MAX_TOOL_CHARS]