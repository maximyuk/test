from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


from keyboards import *




# Функція для того щоб повертатись назад та ховати повідомлення
async def back_kb_dev() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.add(InlineKeyboardButton(text="⬅️ Назад", callback_data="⬅️ Назад"))
    builder.add(InlineKeyboardButton(text="Сховати ❌", callback_data="Сховати ❌"))

    return builder.adjust(2).as_markup()




# Функція щоб сховати повідомлення
async def hide_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.add(InlineKeyboardButton(text="Сховати ❌", callback_data="Сховати ❌"))

    return builder.as_markup()



