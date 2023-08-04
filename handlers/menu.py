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



# Каллбек для кнопки Рецепти страв🍳
@router.callback_query(F.data == "Рецепти страв🍳")
async def strava(query: types.CallbackQuery):
    code_bot = (
        f"Рецепти страв 🍳 \n\n"
        f"Напишіть назву страви до якої вас цікавить рецепт:"

    )
    await query.message.edit_text(code_bot, parse_mode="HTML", disable_web_page_preview=True)
    await query.message.edit_reply_markup(reply_markup=await back_kb_dev())



# Каллбек для кнопки Пошук страви🍴
@router.callback_query(F.data == "Пошук страви🍴")
async def search_strava(query: types.CallbackQuery):
    code_bot = (
        f"Пошук страви🍴 \n\n"
        f"Напишіть назву страви або важливі інгридієнти що входять до цієї страви:\n"
    )
    await query.message.edit_text(code_bot, parse_mode="HTML", disable_web_page_preview=True)
    await query.message.edit_reply_markup(reply_markup=await back_kb_dev())





# Каллбек для кнопки Національні страви🚩
@router.callback_query(F.data == "Національні страви🚩")
async def nation_strava(query: types.CallbackQuery):
    code_bot = (
        f"Національні страви🚩 \n\n"
        f"Виберіть із списку нижче країну в якої вас цікавить національна страва:"
    )
    await query.message.edit_text(code_bot, parse_mode="HTML", disable_web_page_preview=True)
    await query.message.edit_reply_markup(reply_markup=await nation_kb())




# Каллбек для кнопки Каталог страв📖
@router.callback_query(F.data == "Каталог страв📖")
async def search_strava(query: types.CallbackQuery):
    code_bot = (
        f"Каталог страв📖\n\n"
        f"Кнопками нижче ви можете вибрати страву яка вас цікавить,\n також перемикати сторінки за допомогою кнопок нижче"
    )
    await query.message.edit_text(code_bot, parse_mode="HTML", disable_web_page_preview=True)
    await query.message.edit_reply_markup(reply_markup=await back_kb_dev())




# Каллбек для кнопки Запропонувати страву🤔
@router.callback_query(F.data == "Запропонувати страву🤔")
async def search_strava(query: types.CallbackQuery):
    code_bot = (
        f"Запропонувати страву🤔\n\n"
        f"Напишіть назву страви та можливий опис до неї\n"
        f"Після чого ми розглянемо вашу пропозицію"
    )
    await query.message.edit_text(code_bot, parse_mode="HTML", disable_web_page_preview=True)
    await query.message.edit_reply_markup(reply_markup=await back_kb_dev())




# Каллбек для кнопки Донат 🫡
@router.callback_query(F.data == "Донат 🫡")
async def search_strava(query: types.CallbackQuery):
    text = (
        f"Підтримати проєкт можна за:\n\n"
        f"💳 Monobank card : <code>4441 1144 1963 2409</code>\n"
        f"💳 Monobank url : <a href='https://send.monobank.ua/jar/84a5BF2dt7'>monobank</a>\n\n"
        f"❤️ Повернись живим : <a href='https://savelife.in.ua/'>сайт</a>\n\n"
        f"Кошти підуть на оплату хостингу та покращення бота 🌚"
        )
    await query.message.edit_text(text, parse_mode="HTML", disable_web_page_preview=True)
    await query.message.edit_reply_markup(reply_markup=await back_kb_dev())