from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Smile"), KeyboardButton(text="Links")],
        [KeyboardButton(text="Calc"), KeyboardButton(text="Spec. btn")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Choise action from menu",
    selective=True,
)

spec = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Send geo", request_location=True),
            KeyboardButton(text="Send contact", request_contact=True),
            KeyboardButton(text="Send poll", request_poll=KeyboardButtonPollType()),
        ],
        [
            KeyboardButton(text="Back"),
        ],
    ],
    resize_keyboard=True,
)
