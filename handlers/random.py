from aiogram import Router, types
from aiogram.filters.command import Command
import random
import os 

random_router = Router()


@random_router.message(Command("random"))
async def random_handler(message: types.Message):
    dogs_list = os.listdir('images')
    dog = 'images/' + random.choice(dogs_list)
    photo = types.FSInputFile(dog)
    await message.reply_photo(photo=photo, caption="Dog")

