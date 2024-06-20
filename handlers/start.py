from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from bot import database

start_router = Router()


class ReviewStates(StatesGroup):
    name = State()
    contact = State()
    date = State()
    food_quality = State()
    cleanliness = State()
    comment = State()


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
            ],
            [
                types.InlineKeyboardButton(text="Оставить отзыв", callback_data="review")
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
    await callback.message.answer(
        "«Бублик» — небольшое уютное заведение, открывшееся в центре Бишкека. Новое место, в первую очередь, отличает подход к кофейной обжарке, здесь это делается на основе зерен Starbucks.")


@start_router.callback_query(F.data == "address")
async def about_handler(callback: types.CallbackQuery):
    await callback.message.answer("ул. Тоголок Молдо 1, г. Бишкек")


@start_router.callback_query(F.data == "menu")
async def menu_handler(callback: types.CallbackQuery):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Первые блюда"),
                KeyboardButton(text="Напитки"),
                KeyboardButton(text="Десерты")
            ]
        ]
    )
    await callback.message.answer("Выберите категорию меню:", reply_markup=kb)


@start_router.message(F.text == "Первые блюда")
async def first_courses_handler(message: types.Message):
    await message.answer("Первые блюда:\n\n1. Бублик - 300 сом\n2. Солянка - 200 сом\n")


@start_router.message(F.text == "Напитки")
async def drinks_handler(message: types.Message):
    await message.answer("Напитки:\n\n1. Капучино - 150 сом\n2. Латте - 170 сом\n")


@start_router.message(F.text == "Десерты")
async def desserts_handler(message: types.Message):
    await message.answer("Десерты:\n\n1. Торт - 250 сом\n2. Мороженое - 100 сом\n")


@start_router.message(Command("review"))
@start_router.callback_query(F.data == "review")
async def review_handler(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(ReviewStates.name)
    await callback.message.answer("Вы можете остановить в любой момент написав 'стоп'")
    await callback.message.answer("Как Вас зовут?")


@start_router.message(Command("stop"))
@start_router.message(F.text == "стоп")
async def stop_review(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо! Ваш отзыв закончен.")


@start_router.message(ReviewStates.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ReviewStates.contact)
    await message.answer("Оставьте ваш инстаграм:")


@start_router.message(ReviewStates.contact)
async def process_contact(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.text)
    await state.set_state(ReviewStates.date)
    await message.answer("Дата вашего посещения нашего заведения (дд.мм.гггг):")


@start_router.message(ReviewStates.date)
async def process_date(message: types.Message, state: FSMContext):
    if not message.text.replace('.', '').isdigit():
        await message.answer("Пожалуйста, введите дату в формате дд.мм.гггг.")
        return
    await state.update_data(date=message.text)
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="1"),
                KeyboardButton(text="2"),
                KeyboardButton(text="3"),
                KeyboardButton(text="4"),
                KeyboardButton(text="5")
            ]
        ]
    )
    await state.set_state(ReviewStates.food_quality)
    await message.answer("Как оцениваете качество еды? (1-5):", reply_markup=kb)


@start_router.message(ReviewStates.food_quality)
async def process_food_quality(message: types.Message, state: FSMContext):
    if message.text not in ["1", "2", "3", "4", "5"]:
        await message.answer("Пожалуйста, введите оценку от 1 до 5.")
        return
    await state.update_data(food_quality=message.text)
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="1"),
                KeyboardButton(text="2"),
                KeyboardButton(text="3"),
                KeyboardButton(text="4"),
                KeyboardButton(text="5")
            ]
        ]
    )
    await state.set_state(ReviewStates.cleanliness)
    await message.answer("Как оцениваете чистоту заведения? (1-5):", reply_markup=kb)


@start_router.message(ReviewStates.cleanliness)
async def process_cleanliness(message: types.Message, state: FSMContext):
    if message.text not in ["1", "2", "3", "4", "5"]:
        await message.answer("Пожалуйста, введите оценку от 1 до 5.")
        return
    await state.update_data(cleanliness=message.text)
    await state.set_state(ReviewStates.comment)
    await message.answer("Ваши дополнительные комментарии:")


@start_router.message(ReviewStates.comment)
async def process_comment(message: types.Message, state: FSMContext):
    await state.update_data(comment=message.text)
    data = await state.get_data()
    print(data)
    await database.execute("""
        INSERT INTO review_results (name, contact, date, food_quality, cleanliness, comment) 
        VALUES (?, ?, ?, ?, ?, ?)""",
                           (data['name'], data['contact'], data['date'], data['food_quality'], data['cleanliness'],
                            data['comment'])
                           )
    await state.clear()
    await message.answer("Спасибо за ваш отзыв!")
