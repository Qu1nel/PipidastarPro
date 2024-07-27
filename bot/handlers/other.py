from pathlib import Path

from aiogram import F, Router
from aiogram.types import Message
from loguru import logger

import bot.keyboards as kb
from bot.database.json_data import get_content_json_from_file

bot_msg_router = Router(name="bot_msg_router")


@bot_msg_router.message(
    F.text.lower().in_(
        ["привет", "прив", "ку", "здаров", "дратути", "здрасте", "здравствуйте", "здравствуй", "даров", "приветик"],
    ),
)
async def greetings(msg: Message) -> None:
    await msg.reply("дратути ;)")


@bot_msg_router.message()
async def echo(message: Message) -> None:
    msg = message.text.lower() if message.text else "error"
    smiles = await get_content_json_from_file(Path("pages.json"))

    match msg:
        case "links":
            await message.answer("Links:", reply_markup=kb.inlines.links)
        case "spec. btn":
            await message.answer("Spec. btn:", reply_markup=kb.replies.spec)
        case "calc":
            await message.answer("Enter expression:", reply_markup=kb.builders.calc_kb())
        case "smile":
            await message.answer(f"{smiles[1][0]} - <b>{smiles[1][1]}</b>", reply_markup=kb.fabrics.paginator(1))
        case "back":
            await message.answer("Menu", reply_markup=kb.replies.main_menu)
        case _:
            logger.error(f"{msg = }")
