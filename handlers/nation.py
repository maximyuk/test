from aiogram.filters import Command
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove

from aiogram import F, Router, types

from aiogram.types import CallbackQuery, Message
from keyboards import *

router = Router()  

@router.callback_query(F.data == "⬅️ Назад до країн")
async def nation_back(query:CallbackQuery):
	await query.message.edit_text("Національні страви🚩 \n\n Виберіть із списку нижче країну в якої вас цікавить національна страва:")
	await query.message.edit_reply_markup(reply_markup=await nation_kb())




    


@router.callback_query(F.data == "Україна 🇺🇦")
async def ukraine(query: types.CallbackQuery):
    await query.message.edit_text("Українські національні страви", reply_markup=await back_kb_nation())


@router.callback_query(F.data == "Польща 🇵🇱")
async def poland(query: types.CallbackQuery):
    await query.message.edit_text("Польські національні страви", reply_markup=await back_kb_nation())


@router.callback_query(F.data == "Німечинна 🇩🇪")
async def germany(query: types.CallbackQuery):
    await query.message.edit_text("Німецькі національні страви", reply_markup=await back_kb_nation())



@router.callback_query(F.data == "Чехія 🇨🇿")
async def chech(query: types.CallbackQuery):
    await query.message.edit_text("Чеські національні страви", reply_markup=await back_kb_nation())




@router.callback_query(F.data == "Японія 🇯🇵")
async def japan(query: types.CallbackQuery):
    await query.message.edit_text("Японські національні страви", reply_markup=await back_kb_nation())




@router.callback_query(F.data == "Китай 🇨🇳")
async def china(query: types.CallbackQuery):
    await query.message.edit_text("Китайські національні страви", reply_markup=await back_kb_nation())



@router.callback_query(F.data == "Румунія 🇷🇴")
async def romania(query: types.CallbackQuery):
    await query.message.edit_text("Румунські національні страви", reply_markup=await back_kb_nation())



@router.callback_query(F.data == "Молдова 🇲🇩")
async def moldova(query: types.CallbackQuery):
    await query.message.edit_text("Молдовські національні страви", reply_markup=await back_kb_nation())