from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="1"),
                KeyboardButton(text="2"),
                KeyboardButton(text="3"),
                KeyboardButton(text="4"),
                KeyboardButton(text="5")
            ]
        ],
        resize_keyboard=True
    )
