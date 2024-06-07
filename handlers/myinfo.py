from aiogram import Router, types
from aiogram.filters.command import Command


myinfo_router = Router()


@myinfo_router.message(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    info_text = (
        f"Ваш ID: {user_id}\n"
        f"Ваше имя: {first_name}\n"
        f"Ваше имя пользователя: @{username}"
    )
    await message.answer(info_text)

