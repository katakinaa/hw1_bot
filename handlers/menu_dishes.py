from aiogram import Router, types, F
from aiogram.filters.command import Command
import sqlite3


menu_dishes_router = Router()


@menu_dishes_router.message(Command("menu"))
async def show_menu_dishes(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Напитки"),
            ],
            [
                types.KeyboardButton(text="Первые блюда"),
                types.KeyboardButton(text="Вторые блюда"),
            ],
            [
                types.KeyboardButton(text="Десерты")
            ]
        ],
        resize_keyboard=True
    )

    await message.answer("Выберите категорию", reply_markup=kb)


categories = ("напитки", "первые блюда", "вторые блюда", "десерты")


@menu_dishes_router.message(F.text.lower().in_(categories))
async def show_dishes(message: types.Message):
    kb = types.ReplyKeyboardRemove()

    category = message.text
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    query = cursor.execute("SELECT * FROM dishes WHERE category_id = 1")
    dishes = query.fetchall()
    print(dishes)
    await message.answer(f"Блюда из категории {category} ", reply_markup=kb)
