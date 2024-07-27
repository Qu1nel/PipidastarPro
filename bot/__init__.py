import logging
import os

from loguru import logger

from bot.main import start_bot
from bot.misc import config

logging_config = config.logging
bot_config = config.bot

__all__ = ["start_bot", "logging_config", "bot_config"]

logging.basicConfig(**logging_config.base.model_dump())

logger.add(
    f"{logging_config.default_dir}{os.sep}debug.{logging_config.extension_files}",
    level="DEBUG",
    format=logging_config.format_output,
    rotation=logging_config.rotation,
    compression=logging_config.format_compression,
    filter=(lambda record: record["level"].name == "DEBUG"),
    enqueue=True,
)

logger.add(
    f"{logging_config.default_dir}{os.sep}error.{logging_config.extension_files}",
    level="ERROR",
    format=logging_config.format_output,
    rotation=logging_config.rotation,
    compression=logging_config.format_compression,
    backtrace=True,
    diagnose=True,
    filter=(lambda record: record["level"].name == "ERROR"),
    enqueue=True,
)

logger.add(
    f"{logging_config.default_dir}{os.sep}info.{logging_config.extension_files}",
    level="INFO",
    format=logging_config.format_output,
    rotation=logging_config.rotation,
    compression=logging_config.format_compression,
    filter=(lambda record: record["level"].name in ["INFO", "WARNING"]),
    enqueue=True,
)
