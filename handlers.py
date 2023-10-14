from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from text import start_text

router = Router()

set = []


@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer(start_text)
    await msg.answer()


@router.message()
async def message_handler(msg: Message):
    print(msg.from_user.full_name)
    print(((msg.text)))





