from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Pagination(CallbackData, prefix="q"):
    action: str
    page: int


def paginator(page: int = 0) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text=":3", callback_data=Pagination(action="prev", page=page).pack()),
        InlineKeyboardButton(text=".__.", callback_data=Pagination(action="next", page=page).pack()),
        width=2,
    )
    return builder.as_markup(resize_keyboard=True)
