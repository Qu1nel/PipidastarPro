from collections.abc import Sequence
from pathlib import Path

from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from dotenv import find_dotenv, load_dotenv
from pydantic import BaseModel, Field, SecretStr
from pydantic_settings import BaseSettings

from bot.misc.types import HandlerType
from bot.misc.utils import get_handlers_for_filtered

load_dotenv(find_dotenv(".env"))
env_location = Path(".env").resolve()


class BotConfig(BaseSettings):
    token: SecretStr
    properties: DefaultBotProperties = DefaultBotProperties(parse_mode=ParseMode.HTML)

    class Config:
        case_sensitive = False
        env_prefix = "BOT_"
        _env_file = env_location
        _env_file_encoding = "utf-8"


class BaseLoggingConfig(BaseSettings):
    level: int = 0
    force: bool = True
    handlers: Sequence[HandlerType] = Field(default_factory=get_handlers_for_filtered)

    class Config:
        case_sensitive = True
        env_prefix = "LOG_"
        _env_file = env_location
        _env_file_encoding = "utf-8"


class LoggingConfig(BaseModel):
    base: BaseLoggingConfig = Field(default_factory=BaseLoggingConfig)
    format_output: str = "{time} | {level} | {module}:{function}:{line} | {message}"
    rotation: str = "2 MB"
    format_compression: str = "zip"
    default_dir: str = "logs"
    extension_files: str = "log"


class MainBotConfig(BaseSettings):
    bot: BotConfig = Field(default_factory=BotConfig)  # type: ignore
    logging: LoggingConfig = Field(default_factory=LoggingConfig)


_config = MainBotConfig()
