from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central configuration for Multi MCP Agent Router Pro.
    """

    # =========================
    # Project Information
    # =========================
    APP_NAME: str = "Multi MCP Agent Router Pro"
    VERSION: str = "1.0.0"

# =========================
# LLM Providers
# =========================
    OPENROUTER_API_KEY: str = ""


    ANTHROPIC_API_KEY: str = ""
    GITHUB_TOKEN: str = ""

    DEFAULT_PROVIDER: str = "openrouter"
    DEFAULT_MODEL: str = "deepseek/deepseek-r1-0528"
    MAX_TOKENS: int = 1024

    # =========================
    # Workspace
    # =========================
    PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent
    WORKSPACE: Path = PROJECT_ROOT / "workspace"
    LOG_FOLDER: Path = PROJECT_ROOT / "logs"

    # =========================
    # UI
    # =========================
    STREAMING_ENABLED: bool = True

    SHOW_ACTIVITY_PANEL: bool = True

    SHOW_TOOL_STATUS: bool = True

    # =========================
    # MCP
    # =========================
    MCP_TIMEOUT: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


import os

settings = Settings()

print("=" * 80)
print("STARTUP DEBUG")
print("PORT =", os.getenv("PORT"))
print("OPENROUTER_API_KEY exists =", bool(os.getenv("OPENROUTER_API_KEY")))
print("GITHUB_TOKEN exists =", bool(os.getenv("GITHUB_TOKEN")))
print("Provider =", settings.DEFAULT_PROVIDER)
print("Model =", settings.DEFAULT_MODEL)
print("MAX_TOKENS =", settings.MAX_TOKENS)
print("OpenRouter Loaded =", bool(settings.OPENROUTER_API_KEY))
print("Github Loaded =", bool(settings.GITHUB_TOKEN))
print("=" * 80)