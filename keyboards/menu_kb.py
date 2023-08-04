from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



def menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Про бота📎")
    kb.button(text="Допомога🛠")
    kb.button(text="Розробка🧩")
    kb.button(text="Статистика🧮")
    kb.button(text="Стікери👨‍👩‍👧‍👦")
    kb.button(text="Донат🫡")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


async def menu_inline() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    keyboard = [
        "Про бота 🖇",
        "Розробка 🧩",
        "Статистика 🧮",
        "Допомога 🛠",
        "Стікери 👨‍👩‍👧‍👦",
        "Сховати ❌",
        "Донат 🫡",
    ]

    for button in keyboard:
        builder.add(InlineKeyboardButton(text=button, callback_data=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)
















