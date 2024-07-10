from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # type: ignore
from aiogram.utils import executor  # type: ignore

from loguru import logger

from bot.database.models import register_models
from bot.filters import register_all_filters
from bot.handlers import register_all_handlers


async def __on_startup(dp: Dispatcher) -> None:
    register_all_filters(dp)
    register_all_handlers(dp)
    register_models()


@logger.catch()
def start(bt: Bot) -> None:
    """Function to launch a dispatcher for bot."""
    dp = Dispatcher(bt, storage=MemoryStorage())  # type: ignore
    executor.start_polling(dp, skip_updates=True, on_startup=__on_startup)
