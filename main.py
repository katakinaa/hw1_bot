import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
import logging


load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f"Привет, {name}")


@dp.message(Command("myinfo"))
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


@dp.message(Command("random"))
async def random_handler(message: types.Message):
    dogs_list = os.listdir('images')
    dog = 'images/' + random.choice(dogs_list)
    photo = types.FSInputFile(dog)
    await message.reply_photo(photo=photo, caption="Dog")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

