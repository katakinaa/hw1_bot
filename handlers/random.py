from aiogram import Router, types
from aiogram.filters import Command  
import random
import os


random_router = Router()


@random_router.message(Command("random"))
async def random_handler(message: types.Message):
    dishes_list = os.listdir('images')
    dish_file = 'images/' + random.choice(dishes_list)
    dish_name = os.path.basename(dish_file).split('.')[0].capitalize()  
    photo = types.FSInputFile(dish_file)  
    await message.reply_photo(photo=photo, caption=dish_name)