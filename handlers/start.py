from aiogram import Router, types, F
from aiogram.filters.command import Command


start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(text="Наш инстаграм", url="https://www.instagram.com/ya_booblik/")
                ],
                [
                    types.InlineKeyboardButton(text="О нас", callback_data="about"),
                    types.InlineKeyboardButton(text="Наш адрес", callback_data="address")
                ],
                [
                    types.InlineKeyboardButton(text="Наше меню", callback_data="menu")
                ]
            ]
        )

    name = message.from_user.first_name
    await message.answer(
        f"Привет, {name}",
        reply_markup=kb
    )


@start_router.callback_query(F.data == "about")
async def about_handler(callback: types.CallbackQuery):
    await callback.message.answer("«Бублик» — небольшое уютное заведение, открывшееся в центре Бишкека. Новое место, в первую очередь, отличает подход к кофейной обжарке, здесь это делается на основе зерен Starbucks.")


@start_router.callback_query(F.data == "address")
async def about_handler(callback: types.CallbackQuery):
    await callback.message.answer("ул. Тоголок Молдо 1, г. Бишкек")


@start_router.callback_query(F.data == "menu")
async def menu_handler(callback: types.CallbackQuery):
    await callback.message.answer("Наше меню:\n\n 1. Капучино - 150 сом\n 2. Бублик - 200 сом\n 3. Круассан - 100 сом\n")