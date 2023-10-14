from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
from aiogram import types
from test_mat import *

menu = [
[InlineKeyboardButton(text='Вы готовы выбрать челлендж?💪🏻', callback_data= "ready")]]
menu = InlineKeyboardMarkup(inline_keyboard=menu)

kb_ready = [
    [InlineKeyboardButton(text="Да", callback_data="ready_yes"),
     InlineKeyboardButton(text="Нет", callback_data="ready_no")],
    ]

kb_ready_state = InlineKeyboardMarkup(inline_keyboard=kb_ready)

kb_info = [
    [InlineKeyboardButton(text="Введите кол-во отжиманий ", callback_data="pushups"),
    InlineKeyboardButton(text="Введите кол-во подтягиваний ", callback_data="pullups")],
    [InlineKeyboardButton(text="Приседания", callback_data="squats"),
    InlineKeyboardButton(text="Время в планке (в сек.)", callback_data="plank")],
]

kb_info_state = InlineKeyboardMarkup(inline_keyboard=kb_info)


# @dispatcher.callback_query_handler(lambda c: c.data == 'ready')
# async def process_callback_button(message: types.Message, callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await message.answer(
#         reply_markup=kb.kb_ready_state,
#     )

@dispatcher.callback_query(lambda c: c.data == 'ready')
async def process_callback_button(message: types.Message, callback_query: types.CallbackQuery):
    #await bot.answer_callback_query(callback_query.id)
    await message.answer(
        "Готов к марафону?",
        reply_markup=kb.menu,
    )