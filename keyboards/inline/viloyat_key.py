from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

villar = InlineKeyboardMarkup(
    inline_keyboard= [ 
        [ 
            InlineKeyboardButton("Namangan", callback_data='nam'),
            InlineKeyboardButton("Andijon", callback_data='and')
        ],
        [ 
            InlineKeyboardButton("Toshkent", callback_data='tos'),
            InlineKeyboardButton("Farg'ona", callback_data='far')
        ],
        [ 
            InlineKeyboardButton("Qashqadaryo", callback_data='qas'),
            InlineKeyboardButton("Surxondaryo", callback_data='sur')
        ],
        [ 
            InlineKeyboardButton("Samarqand", callback_data='sam'),
            InlineKeyboardButton("Buxoro", callback_data='bux')
        ],
        [ 
            InlineKeyboardButton("Navoiy", callback_data='nav'),
            InlineKeyboardButton("Sirdaryo", callback_data='sir')
        ],
        [ 
            InlineKeyboardButton("Jizzax", callback_data='jiz'),
            InlineKeyboardButton("Xorazm", callback_data='xor')
        ],
        [ 
            InlineKeyboardButton("Qoraqalpog'iston", callback_data='qor')
        ]
    ],row_width=2
)