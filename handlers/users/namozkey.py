from aiogram.types import Message
from loader import dp 
from aiogram.dispatcher.filters.builtin import Text
from keyboards.inline.viloyat_key import villar


@dp.message_handler(Text(equals='⏰Namoz vaqtlari'))
async def namoz(ms:Message):
    await ms.answer("📍Kerak bo'lgan viloyat nomini tanlang: ", reply_markup=villar)











