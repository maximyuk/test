
from aiogram.filters import Command
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove

from aiogram import F, Router, types


from aiogram.types import CallbackQuery, Message

from keyboards import *

router = Router()  # [1]


# Сховати ❌ (Використовується скрізь)
@router.callback_query(F.data == "Сховати ❌")
async def hide_message(query: CallbackQuery):
    await query.message.delete()



@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer("Вас вітає цей прикрасний бот", reply_markup=await menu_inline())



# Про бота 🖇
@router.callback_query(F.data == "Розробка 🧩")
async def code_bot(query: types.CallbackQuery):
    code_bot = (
        f"🤖 БОТ \n"
        f"🆙 Версія : release 0.0\n"
        f"👨‍💻 Розробник: \n"
        f"👨‍💻 Бот на стадії повної розробки\n"
    )
    await query.message.edit_text(code_bot, parse_mode="HTML", disable_web_page_preview=True)
    await query.message.edit_reply_markup(reply_markup=await back_kb_dev())