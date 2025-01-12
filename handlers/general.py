from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
# from model.feedback import Feedback
from keyboards import get_general_kb, get_scores_keyboard

class GeneralStates(StatesGroup):
    start = State()
    registration = State()
    login = State()


router = Router()


@router.message(StateFilter(None), Command('start'))
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('Привет, я создан для спорта. Для регистрации напишите \n/registration\n'
                         'если уже зарегестрированы напишите \n/login\n'
                         'или нажмите соответствующие кнопки', reply_markup=get_general_kb())
    await state.set_state(GeneralStates.start)





# @router.message(StateFilter(None), Command('Оставить_отзыв', 'feedback'))
# async def feedback_handler(message: types.Message, state: FSMContext):
#
#     await message.answer('Введи своё общее впечатление.\n'
#                          'Можно использовать только текст!')
#     await state.set_state(FeedbackStates.impression)
#
# @router.message(StateFilter(FeedbackStates.impression), F.text)
# async def impression_handler(message: types.Message, state: FSMContext):
#     await message.answer('Спасибо за ваш ответ.\n'
#                          'Теперь оцените по шкале от 1 до 5.\n'
#                          'Здесь можно ввести цифры и только цифры.\n'
#                          'Ну может ещё клавиатура появится снизу.\n'
#                          'Но это не точно.\n'
#                          'Спасибо за понимание.\n',
#                          reply_markup=get_scores_keyboard())
#
#     await state.set_state(FeedbackStates.rating)
#     user_impression = message.text
#     await state.update_data(impression=user_impression)
#
#
#
#
# @router.message(StateFilter(FeedbackStates.rating), lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 5)
# async def rating_handler(message: types.Message, state: FSMContext):
#     await message.answer('Спасибо за вашу оценку.\n'
#                          'Теперь введите коментарий по этому поводу или по другому.\n'
#                          'Да вообще, вводите что хотите, но помните что только текст!')
#     await state.set_state(FeedbackStates.comment)
#     user_score = message.text
#     await state.update_data(score=user_score)
#
#
# @router.message(StateFilter(FeedbackStates.rating), F)
# async def rating_handler(message: types.Message, state: FSMContext):
#     await message.answer('Вы ввели не ту оценку, введите заново свою оценку от 1 до 5')
#
#
# @router.message(StateFilter(FeedbackStates.comment), F.text)
# async def comment_handler(message: types.Message, state: FSMContext):
#     await message.answer('Спасибо за ваш комментарий. \n'
#                          'Ваш отзыв добавлен в общую базу.\n'
#                          'Удачного дня. И совет дня.\n'
#                          'Не ешьте жёлтый снег ;)')
#     user_comment = message.text
#     await state.update_data(comment=user_comment)
#     data = await state.get_data()
#     full_feedback = Feedback(data["impression"], data["score"], data["comment"])
#     storage.append(full_feedback)
#     await state.clear()
#
# @router.message(StateFilter(FeedbackStates.impression, FeedbackStates.comment))
# async def error_type_impression_handler(message: types.Message, state: FSMContext):
#     await message.answer('Вы чем читаете?\n'
#                          'Впечатление можно выразить только текстом.\n'
#                          'Пожалуйста введите своё впечатление и отправьте ещё раз.\n'
#                          'Спасибо.')
#
# @router.message(Command('show', 'Покажи_отзывы'))
# async def show_handler(message: types.Message):
#     if len(storage) == 0:
#         await message.answer(f'Отзывов нет. Извините')
#         return
#
#     await message.answer(f'Все отзывы:\n')
#     for feedback in storage:
#         await message.answer(f'{feedback}')

