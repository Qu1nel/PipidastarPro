from aiogram import Dispatcher
from aiogram.types import Message


async def echo(msg: Message) -> None:
    await msg.answer(msg.text)


def register_other_handlers(dp: Dispatcher) -> None:
    # register all other handlers
    dp.register_message_handler(echo, content_types=["text"])
