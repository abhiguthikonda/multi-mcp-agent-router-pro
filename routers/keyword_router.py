from agents import registry


class KeywordRouter:
    """
    Fast rule-based routing.
    """

    def __init__(self):
        self.security_keywords = {
            "security",
            "vulnerability",
            "owasp",
            "xss",
            "csrf",
            "secret",
            "authentication",
            "authorization",
            "sql injection",
        }

        self.code_keywords = {
            "code",
            "review",
            "bug",
            "python",
            "java",
            "javascript",
            "function",
            "class",
            "repository",
            "github",
            "pull request",
        }

        self.bim_keywords = {
            "bim",
            "revit",
            "construction",
            "building",
            "architecture",
        }

    def route(self, prompt: str):

        text = prompt.lower()

        if any(word in text for word in self.security_keywords):
            return registry.get("security")

        if any(word in text for word in self.code_keywords):
            return registry.get("code_reviewer")

        if any(word in text for word in self.bim_keywords):
            return registry.get("bim")

        return registry.get("researcher")