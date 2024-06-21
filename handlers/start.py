from aiogram import Router, types, F
from aiogram.filters.command import Command
from keyboards.kb_start import kb_1, kb_2


start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f"Привет, {name}", reply_markup=kb_1)


@start_router.callback_query(F.data == "about")
async def about_handler(callback: types.CallbackQuery):
    await callback.message.answer("«Бублик» — небольшое уютное заведение, открывшееся в центре Бишкека. Новое место, в первую очередь, отличает подход к кофейной обжарке, здесь это делается на основе зерен Starbucks.")


@start_router.callback_query(F.data == "address")
async def about_handler(callback: types.CallbackQuery):
    await callback.message.answer("ул. Тоголок Молдо 1, г. Бишкек")


@start_router.callback_query(F.data == "menu")
async def menu_handler(callback: types.CallbackQuery):
    await callback.message.answer("Выберите категорию меню:", reply_markup=kb_2)


@start_router.message(F.text == "Первые блюда")
async def first_courses_handler(message: types.Message):
    await message.answer("Первые блюда:\n\n1. Бублик - 300 сом\n2. Солянка - 200 сом\n")


@start_router.message(F.text == "Напитки")
async def drinks_handler(message: types.Message):
    await message.answer("Напитки:\n\n1. Капучино - 150 сом\n2. Латте - 170 сом\n")


@start_router.message(F.text == "Десерты")
async def desserts_handler(message: types.Message):
    await message.answer("Десерты:\n\n1. Торт - 250 сом\n2. Мороженое - 100 сом\n")



