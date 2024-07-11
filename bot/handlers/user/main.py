import random

from aiogram import Router, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.enums.dice_emoji import DiceEmoji

from loguru import logger

import bot.keyboards as kb

user_router = Router(name="user_router")


@user_router.message(CommandStart())
async def start(message: Message) -> None:
    msg = f"мяяяя, {message.from_user.first_name}" if message.from_user else "NIGA"
    await message.answer(msg, reply_markup=kb.replies.main_menu)


@user_router.message(Command("play"))
async def play(message: Message) -> None:
    x = await message.answer_dice(DiceEmoji.DICE)
    dice_value = x.dice.value if x.dice else -1
    logger.debug(f"{dice_value = }")


@user_router.message(Command(commands=["rand", "random", "rnum"]))
async def get_random_numbr(msg: Message, command: CommandObject) -> None:
    if command.args:
        num = random.randint(*(int(n) for n in command.args.split("-")))
        await msg.reply(f"Random number: {num}")


def register_user_handlers(dp: Dispatcher) -> None:
    dp.include_router(user_router)
