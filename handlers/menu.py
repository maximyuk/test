from aiogram.filters import Command
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove

from aiogram import F, Router, types

from aiogram.types import CallbackQuery, Message
from keyboards import *

router = Router()  # [1]


# Повертає інлайн до меню команди /start
@router.callback_query(F.data == "⬅️ Назад")
async def back_menu(query: CallbackQuery):
    await query.message.edit_text("🤖 БОТ СТРАВИ \n 🆙 У цьома боті є різноманітна кількість страв\n\n 🍳 Рецепти страв - У цьому розділі ви зможете побачити самі популярні рецепти страв!\n 🍴 Пошук страви - У цьому розділі ви зможете знайти страву за її назвою та побачити її фото та опис\n 🚩 Національні страви - У цьому розділі зможете вибрати країну та побачити її самі популярні національні страви\n 📖 Каталог страв - У цьому розділі зібрані всі страви\n 🤔 Запропонувати страву - Не знайшли страву що вам потрібна? Тоді ви самі можете запропонувати а ми її добавимо \n 🫡 Донат - Хочете підтримати наш проєкт? Тоді нажимай на цю кнопку \n", reply_markup=await menu_inline())




# Сховати ❌ (Використовується скрізь)
@router.callback_query(F.data == "Сховати ❌")
async def hide_message(query: CallbackQuery):
    await query.message.delete()






@router.message(Command("start")) 
async def cmd_start(message: Message):
    await message.answer("🤖 БОТ СТРАВИ \n 🆙 У цьома боті є різноманітна кількість страв\n\n 🍳 Рецепти страв - У цьому розділі ви зможете побачити самі популярні рецепти страв!\n 🍴 Пошук страви - У цьому розділі ви зможете знайти страву за її назвою та побачити її фото та опис\n 🚩 Національні страви - У цьому розділі зможете вибрати країну та побачити її самі популярні національні страви\n 📖 Каталог страв - У цьому розділі зібрані всі страви\n 🤔 Запропонувати страву - Не знайшли страву що вам потрібна? Тоді ви самі можете запропонувати а ми її добавимо \n 🫡 Донат - Хочете підтримати наш проєкт? Тоді нажимай на цю кнопку \n", reply_markup=await menu_inline())



# Каллбек для кнопки Розробка🧩
@router.callback_query(F.data == "Рецепти страв🍳")
async def strava(query: types.CallbackQuery):
    code_bot = (
        f"🤖 Рецепти страв \n"
    )
    await query.message.edit_text(code_bot, parse_mode="HTML", disable_web_page_preview=True)
    await query.message.edit_reply_markup(reply_markup=await back_kb_dev())



# Каллбек для кнопки Розробка🧩
@router.callback_query(F.data == "Пошук страви🍴")
async def strava(query: types.CallbackQuery):
    code_bot = (
        f"🤖 Пошук \n"
    )
    await query.message.edit_text(code_bot, parse_mode="HTML", disable_web_page_preview=True)
    await query.message.edit_reply_markup(reply_markup=await back_kb_dev())