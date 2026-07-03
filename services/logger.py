import logging
from pathlib import Path

from config.settings import settings


def setup_logger() -> logging.Logger:
    """
    Configure and return the application's logger.
    """

    settings.LOG_FOLDER.mkdir(exist_ok=True)

    log_file = settings.LOG_FOLDER / "agent.log"

    logger = logging.getLogger("multi_mcp_router")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


logger = setup_logger()