from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard= [ 
        [ 
            InlineKeyboardButton("Bugungi Namoz vaqtlari", callback_data='bugungi'),
            InlineKeyboardButton("Ertangi Namoz vaqtlari", callback_data='ertangi')
        ],
        [ 
            InlineKeyboardButton("Haftalik Namoz vaqtlari", callback_data='hafta')
        ]
    ]
)