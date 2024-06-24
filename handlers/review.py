from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.kb_review import kb
from bot import database


review_router = Router()


class ReviewStates(StatesGroup):
    name = State()
    contact = State()
    date = State()
    food_quality = State()
    cleanliness = State()
    comment = State()


@review_router.message(Command("review"))
async def review_handler(message: types.Message, state: FSMContext):
    await state.set_state(ReviewStates.name)
    await message.answer("Вы можете остановить в любой момент написав 'стоп'")
    await message.answer("Как Вас зовут?")


@review_router.message(Command("stop"))
@review_router.message(F.text == "стоп")
async def stop_review(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо! Ваш отзыв закончен.")


@review_router.message(ReviewStates.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ReviewStates.contact)
    await message.answer("Оставьте ваш инстаграм:")


@review_router.message(ReviewStates.contact)
async def process_contact(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.text)
    await state.set_state(ReviewStates.date)
    await message.answer("Дата вашего посещения нашего заведения (дд.мм.гггг):")


@review_router.message(ReviewStates.date)
async def process_date(message: types.Message, state: FSMContext):
    if not message.text.replace('.', '').isdigit():
        await message.answer("Пожалуйста, введите дату в формате дд.мм.гггг.")
        return
    await state.update_data(date=message.text)
    await state.set_state(ReviewStates.food_quality)
    await message.answer("Как оцениваете качество еды? (1-5):", reply_markup=kb)


@review_router.message(ReviewStates.food_quality)
async def process_food_quality(message: types.Message, state: FSMContext):
    if message.text not in ["1", "2", "3", "4", "5"]:
        await message.answer("Пожалуйста, введите оценку от 1 до 5.")
        return
    await state.update_data(food_quality=message.text)
    await state.set_state(ReviewStates.cleanliness)
    await message.answer("Как оцениваете чистоту заведения? (1-5):", reply_markup=kb)


@review_router.message(ReviewStates.cleanliness)
async def process_cleanliness(message: types.Message, state: FSMContext):
    if message.text not in ["1", "2", "3", "4", "5"]:
        await message.answer("Пожалуйста, введите оценку от 1 до 5.")
        return
    await state.update_data(cleanliness=message.text)
    await state.set_state(ReviewStates.comment)
    await message.answer("Ваши дополнительные комментарии:")


@review_router.message(ReviewStates.comment)
async def process_comment(message: types.Message, state: FSMContext):
    await state.update_data(comment=message.text)
    data = await state.get_data()
    await database.execute("""
        INSERT INTO review_results (name, contact, date, food_quality, cleanliness, comment) 
        VALUES (?, ?, ?, ?, ?, ?)""",
                           (data['name'], data['contact'], data['date'], data['food_quality'], data['cleanliness'],
                            data['comment'])
                           )
    await state.clear()
    await message.answer("Спасибо за ваш отзыв!")
