from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

home = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

namozi = KeyboardButton("⏰Namoz vaqtlari")

home.insert(namozi)