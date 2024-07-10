from collections.abc import Sequence
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

from bot.misc.types import HandlerType
from bot.misc.utils import get_handlers_for_filtered

__all__ = ["_config"]

load_dotenv()
env_location = Path(".env").resolve()


class BotConfig(BaseSettings):
    """Bot configuration storage class.

    Attributes:
        token - A secret token for bot.
    """

    token: str

    class Config:
        case_sensitive = True
        env_prefix = "BOT_"
        _env_file = env_location
        _env_file_encoding = "utf-8"


class BaseLoggingConfig(BaseSettings):
    """Base logging config."""

    level: int = 0
    force: bool = True
    handlers: Sequence[HandlerType] = Field(default_factory=get_handlers_for_filtered)

    class Config:
        case_sensitive = True
        env_prefix = "LOG_"
        _env_file = env_location
        _env_file_encoding = "utf-8"


class LoggingConfig(BaseModel):
    """Initialization class for logging."""

    base: BaseLoggingConfig = Field(default_factory=BaseLoggingConfig)
    format_output: str = "{time} | {level} | {module}:{function}:{line} | {message}"
    rotation: str = "2 MB"
    format_compression: str = "zip"
    default_dir: str = "logs"
    extension_files: str = "log"


class MainBotConfig(BaseSettings):
    """Main configuration storage class."""

    bot: BotConfig = Field(default_factory=BotConfig)  # type: ignore
    logging: LoggingConfig = Field(default_factory=LoggingConfig)


_config = MainBotConfig()
