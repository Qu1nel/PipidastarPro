from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def calc_kb() -> ReplyKeyboardMarkup:
    items = ["7", "8", "9", "*", "4", "5", "6", "/", "1", "2", "3", "-", "0", ".", "=", "+"]
    builder = ReplyKeyboardBuilder()

    for item in items:
        builder.button(text=item)

    builder.button(text="Back")
    builder.adjust(4, 4, 4, 4, 1)

    return builder.as_markup(resize_keyboard=True)
