from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="youtube", url="https://youtube.com"),
            InlineKeyboardButton(text="Q", url="https://github.com/Qu1nel"),
            InlineKeyboardButton(text="TG", url="tg://resolve?domain=xor_journal"),
        ],
    ],
)
