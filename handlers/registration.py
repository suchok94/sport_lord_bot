from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from .general import GeneralStates
# from .db_functions import

# from model.feedback import Feedback
from keyboards import get_general_kb, get_scores_keyboard

class RegistrationStates(StatesGroup):
    registration = State()

router = Router()

@router.message(StateFilter(GeneralStates.start), Command('registration'))
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('регистрация!')