import logging
import os

from loguru import logger
from aiogram import Bot

from bot.misc import cfg
from bot.main import start as _start

logging_config = cfg.logging
bot_config = cfg.bot

logging.basicConfig(**logging_config.base.model_dump())

logger.add(
    f"{logging_config.default_dir}{os.sep}debug.{logging_config.extension_files}",
    level="DEBUG",
    format="",
    rotation=logging_config.rotation,
    compression=logging_config.format_compression,
    filter=(lambda record: record["level"].name == "DEBUG"),
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
)

logger.add(
    f"{logging_config.default_dir}{os.sep}info.{logging_config.extension_files}",
    level="INFO",
    format=logging_config.format_output,
    rotation=logging_config.rotation,
    compression=logging_config.format_compression,
    filter=(lambda record: record["level"].name in ["INFO", "WARNING"]),
)


def _init_bot() -> Bot:
    return Bot(token=bot_config.token, parse_mode="HTML")


def start_bot() -> None:
    """Function to launch a single bot instance."""
    _start(bt=_init_bot())
