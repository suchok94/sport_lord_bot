from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from keyboards import get_general_kb, get_scores_keyboard


class GeneralStates(StatesGroup):
    start = State()
    registration = State()
    login = State()


router = Router()


@router.message(StateFilter(None), Command('start'))
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer(f'{message.chat.id}')
    await message.answer('Привет, я создан для спорта. Для регистрации напишите \n/registration\n'
                         'если уже зарегестрированы напишите \n/login\n'
                         'или нажмите соответствующие кнопки', reply_markup=get_general_kb())
    await state.set_state(GeneralStates.start)


@router.message(Command('help'))
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('Помогити')