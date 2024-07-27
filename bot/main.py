from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from loguru import logger

from bot.callbacks import register_all_callbacks
from bot.handlers import register_all_handlers
from bot.misc import config


class ClientBot:
    bot: Bot
    dp: Dispatcher

    def __init__(self, token: str, default: DefaultBotProperties | None = None) -> None:
        self.bot = Bot(token=token, default=default)

    def init(self, dispatcher: Dispatcher) -> None:
        self.dp = dispatcher
        for register in (register_all_handlers, register_all_callbacks):
            register(self.dp)


@logger.catch()
async def start_bot() -> None:
    client_bot = ClientBot(token=config.bot.token.get_secret_value(), default=config.bot.properties)
    client_bot.init(dispatcher=Dispatcher())

    await client_bot.bot.delete_webhook(drop_pending_updates=True)
    await client_bot.dp.start_polling(client_bot.bot)
