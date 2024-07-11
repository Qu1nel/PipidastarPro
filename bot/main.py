from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from bot.misc import cfg
from bot.handlers import register_all_handlers
from bot.callbacks import register_all_callbacks


def on_startup(dp: Dispatcher) -> None:
    register_all_handlers(dp)
    register_all_callbacks(dp)


async def start_bot() -> None:
    """Function to launch a single bot instance."""
    bot = Bot(token=cfg.bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    on_startup(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
