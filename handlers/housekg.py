from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from crawler.housekg import get_page, get_links

house_router = Router()


@house_router.message(Command("obyavlenia"))
async def show_obyavlenia(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="парсинг", callback_data="parse_house_kg")
            ]
        ],
        resize_keyboard=True
    )

    await message.answer("Тут будут объявления", reply_markup=kb)


@house_router.callback_query(F.data == "parse_house_kg")
async def parse_house_kg(callback: types.CallbackQuery):
    await callback.answer()
    page = get_page()
    links = get_links(page)
    for link in links:
        await callback.message.answer(link)
