from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
menu = [
[InlineKeyboardButton(text='Вы готовы выбрать челлендж?💪🏻', callback_data="Выберите тип челленджа")]]
menu = InlineKeyboardMarkup(inline_keyboard=menu)