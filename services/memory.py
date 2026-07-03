from collections import defaultdict


class MemoryManager:
    """
    Stores conversation history separately for each agent.
    """

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

        self._history[agent_id].append(
            {
                "role": role,
                "content": content,
            }
        )

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