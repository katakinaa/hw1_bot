import asyncio
import logging
from aiogram import types

from bot import dp, bot, database
from handlers import (
    start_router,
    myinfo_router,
    random_router,
    review_router,
    menu_dishes_router,
    house_router
)


async def on_startup(bot):
    await database.create_tables()


async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="review", description="Оставьте отзыв"),
        types.BotCommand(command="myinfo", description="Информация о вас"),
        types.BotCommand(command="menu", description="Меню"),
        types.BotCommand(command="obyavlenia", description="Показать объявления")
    ])

    dp.include_router(start_router)
    dp.include_router(random_router)
    dp.include_router(myinfo_router)
    dp.include_router(review_router)
    dp.include_router(menu_dishes_router)
    dp.startup.register(on_startup)
    dp.include_router(house_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
