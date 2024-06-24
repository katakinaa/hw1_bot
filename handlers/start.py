from aiogram import Router, types, F
from aiogram.filters.command import Command
from keyboards.kb_start import kb_1


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
