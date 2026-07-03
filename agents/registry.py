from agents.code_reviewer import CodeReviewerAgent
from agents.researcher import ResearchAgent
from agents.security import SecurityAgent
from agents.bim import BIMAgent


class AgentRegistry:
    """
    Stores and manages all available AI agents.
    """

    def __init__(self):
        self._agents = {
            "code_reviewer": CodeReviewerAgent(),
            "researcher": ResearchAgent(),
            "security": SecurityAgent(),
            "bim": BIMAgent(),
        }

    def get(self, agent_id: str):
        """
        Return an agent by its ID.
        """
        return self._agents.get(agent_id)

    def all(self):
        """
        Return all registered agents.
        """
        return list(self._agents.values())

    def ids(self):
        """
        Return all available agent IDs.
        """
        return list(self._agents.keys())