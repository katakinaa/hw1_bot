from aiogram import types


kb_1 = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://www.instagram.com/ya_booblik/")
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about"),
                types.InlineKeyboardButton(text="Наш адрес", callback_data="address")
            ]
        ],
        resize_keyboard=True
    )


kb_2 = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Первые блюда"),
                types.KeyboardButton(text="Напитки"),
                types.KeyboardButton(text="Десерты")
            ]
        ],
        resize_keyboard=True
    )
