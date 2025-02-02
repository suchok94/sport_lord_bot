from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from .general import GeneralStates
from .db_functions import DB

# from .db_functions import

# from model.feedback import Feedback
from keyboards import get_general_kb, get_scores_keyboard, get_yes_no_kb

class RegistrationStates(StatesGroup):
    registration = State()
    name = State()
    verification = State()
    password = State()
    final = State()
    

router = Router()


@router.message(StateFilter(GeneralStates.start), Command('registration'))
async def start_handler(message: types.Message, state: FSMContext):
    # провеку встроить на зарегестрированного пользователя
    await message.answer('Регистрация!, для продолжения введите имя')
    await state.update_data(id= message.chat.id)
    await state.set_state(RegistrationStates.name)

@router.message(StateFilter(RegistrationStates.name), F.text)
async def name_handler(message: types.Message, state: FSMContext):
    await state.update_data(name= message.text)
    await message.answer('Хорошо, теперь нужен ли пароль?', reply_markup=get_yes_no_kb()) # клавиатура да/нет
    await state.set_state(RegistrationStates.verification)

@router.message(StateFilter(RegistrationStates.verification), F.text.lower()=='да')
async def password_handler(message: types.Message, state: FSMContext):
    await message.answer('Раз он нужен, то введи пароль')
    await state.update_data(verification= True)
    await state.set_state(RegistrationStates.password)

@router.message(StateFilter(RegistrationStates.verification), F.text.lower()=='нет')
async def password_handler(message: types.Message, state: FSMContext):
    await state.update_data(verification= False)
    await state.set_state(RegistrationStates.final)

@router.message(StateFilter(RegistrationStates.password), F.text)
async def password_handler(message: types.Message, state: FSMContext):
    await message.answer('Пароль сохранён')
    await state.update_data(password= message.text)
    await state.set_state(RegistrationStates.final)

@router.message(StateFilter(RegistrationStates.final), F.text)
async def final_registration(message: types.Message, state:FSMContext):
    await message.answer('Регистрация завершена')
    data = await state.get_data()
    await DB.add_user(db, data)
    await state.clear()
