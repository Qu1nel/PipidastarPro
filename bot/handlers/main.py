from aiogram import Dispatcher

from bot.handlers.other import bot_msg_router
from bot.handlers.user.main import user_router


def register_user_handlers(dp: Dispatcher) -> None:
    dp.include_router(user_router)


def register_other_handlers(dp: Dispatcher) -> None:
    dp.include_router(bot_msg_router)
