import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup

import kb

bot = Bot(token="5735624284:AAF1vBH4IhF7F2ehDniaQrTRiQJWbugB9As")
dispatcher = Dispatcher()
router = Router()

class Form(StatesGroup):
    name = State()
    age = State()

@dispatcher.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer(
        "Привет, как тебя зовут?",
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.get_data()

@dispatcher.message()
async def process(message: types.Message):
    await message.answer(
        "Готов к марафону?",
        reply_markup=kb.menu,
    )

async def main():
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
