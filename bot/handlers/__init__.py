from aiogram import Dispatcher

from bot.handlers.main import register_other_handlers, register_user_handlers

REGISTER_CALLBACKS_HANDLERS = [
    register_user_handlers,
    register_other_handlers,
]


def register_all_handlers(dp: Dispatcher) -> None:
    for handler in REGISTER_CALLBACKS_HANDLERS:
        handler(dp)
