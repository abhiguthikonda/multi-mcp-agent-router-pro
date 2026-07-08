from collections import defaultdict


class MemoryManager:
    """
    Stores conversation history separately for each agent.
    Automatically limits history size to reduce token usage.
    """

    # Maximum messages stored per agent
    MAX_HISTORY = 20

    def __init__(self):
        self._history = defaultdict(list)

    def add_message(
        self,
        agent_id: str,
        role: str,
        content: str,
    ):
        """
        Add a message to an agent's conversation.
        """

        history = self._history[agent_id]

        history.append(
            {
                "role": role,
                "content": content,
            }
        )

        # Keep only the latest messages
        if len(history) > self.MAX_HISTORY:
            history.pop(0)

    def get_history(self, agent_id: str):
        """
        Return conversation history for an agent.
        """

        return self._history[agent_id]

    def clear(self, agent_id: str):
        """
        Clear one agent's history.
        """

        self._history[agent_id].clear()

    def clear_all(self):
        """
        Clear every conversation.
        """

        self._history.clear()