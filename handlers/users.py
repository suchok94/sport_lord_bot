from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from general import GeneralStates
# from model.feedback import Feedback
from keyboards import get_general_kb, get_scores_keyboard

class UserStates(StatesGroup):
    registration = State()
    login = State()
    comment = State()

router = Router()