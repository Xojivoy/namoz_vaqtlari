from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

villar = InlineKeyboardMarkup(
    inline_keyboard= [ 
        [ 
            InlineKeyboardButton("Namangan", callback_data='namangan'),
            InlineKeyboardButton("Andijon", callback_data='andijon')
        ],
        [ 
            InlineKeyboardButton("Toshkent", callback_data='tashkent'),
            InlineKeyboardButton("Farg'ona", callback_data='ferghana')
        ],
        [ 
            InlineKeyboardButton("Qashqadaryo", callback_data='kashkadarya'),
            InlineKeyboardButton("Surxondaryo", callback_data='surkhandarya')
        ],
        [ 
            InlineKeyboardButton("Samarqand", callback_data='samarkand'),
            InlineKeyboardButton("Buxoro", callback_data='bukhara')
        ],
        [ 
            InlineKeyboardButton("Navoiy", callback_data='navoiy'),
            InlineKeyboardButton("Sirdaryo", callback_data='sirdaryo')
        ],
        [ 
            InlineKeyboardButton("Jizzax", callback_data='jizzakh'),
            InlineKeyboardButton("Xorazm", callback_data='khorezm')
        ],
        [ 
            InlineKeyboardButton("Qoraqalpog'iston", callback_data='qoraqalpogiston')
        ]
    ],row_width=2
)
