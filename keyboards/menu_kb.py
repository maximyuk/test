from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



# Создаєм кнопки для дефолд кнопок в меню
def menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Рецепти страв🍳")
    kb.button(text="Пошук страви🍴")
    kb.button(text="Національні страви🚩")
    kb.button(text="Запропонувати страву🤔")
    kb.button(text="Каталог страв📖")
    kb.button(text="Донат🫡")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)




# Создаєм інлайн кнопки для меню
async def menu_inline() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    keyboard = [
        "Рецепти страв🍳",
        "Пошук страви🍴",
        "Національні страви🚩",
        "Каталог страв📖",
        "Запропонувати страву🤔",
        "Донат 🫡",
        "Сховати ❌",
    ]

    for button in keyboard:
        builder.add(InlineKeyboardButton(text=button, callback_data=button))

    return builder.adjust(2).as_markup(resize_keyboard=True)
















