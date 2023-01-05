from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from keyboards.inline.viloyat_key import villar


@dp.message_handler(CommandStart())
async def bot_start(ms : Message):
    text = "Xush kelibsiz✋ (*￣3￣)╭"
    text += "\n•Men Namoz vaqtlarini aytuvchi bot man sizga namoz o'qishingiz uchun sizga to'g'ri vaqtni aytaman✅ ^_~"
    # text += "\n‣Men har kuni sizga 20:00 da ertangilik namoz vaqtlarini yuboraman"
    # text += "\n»Va qaysidir namoz vaqti boshlanishidan 10daqiqa oldin sizga xabar beraman"
    text += "\n ⁂Bizdan uzoqlashmang biz har doim siz bilanmiz™ ;)"
    await ms.answer(text)
    await ms.answer("O'zingizni viloyatingizni tanlang ☺", reply_markup=villar)




