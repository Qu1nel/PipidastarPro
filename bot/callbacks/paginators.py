from contextlib import suppress
from pathlib import Path

from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from bot.misc.types import KbPaginatorType
from bot.database.json_data import get_content_json_from_file

import bot.keyboards as kb


async def pagination_handler(query: CallbackQuery, callback_data: KbPaginatorType) -> None:
    smiles = await get_content_json_from_file(Path("pages.json"))
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0

    if callback_data.action == "next":
        page = page_num + 1 if page_num < (len(smiles) - 1) else page_num

    if query.message:
        with suppress(TelegramBadRequest):
            await query.message.edit_text(  # type: ignore
                text=f"{smiles[page][0]} - <b>{smiles[page][1]}</b>",
                reply_markup=kb.fabrics.paginator(page),
            )
    await query.answer()
