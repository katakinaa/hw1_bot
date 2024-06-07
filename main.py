import asyncio
import logging
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
from os import getenv


from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.random import random_router
 

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


async def main():
    dp.include_router(start_router)
    dp.include_router(random_router)
    dp.include_router(myinfo_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

