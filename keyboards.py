from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
info = [
    [InlineKeyboardButton(text="Введите кол-во отжиманий ", callback_data="generate_text"),
    InlineKeyboardButton(text="Введите кол-во подтягиваний ", callback_data="generate_image")],
    [InlineKeyboardButton(text="Приседания", callback_data="buy_tokens"),
    InlineKeyboardButton(text="Время в планке (в сек.)", callback_data="balance")],
]

kb_ready = [
        [InlineKeyboardButton(text="Да")],
        [InlineKeyboardButton(text="Нет(")]
    ]

print_info = InlineKeyboardMarkup(inline_keyboard=info)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

