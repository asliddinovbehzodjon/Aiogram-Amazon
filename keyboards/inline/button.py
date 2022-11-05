from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
btn = InlineKeyboardMarkup(
    inline_keyboard= [
        [InlineKeyboardButton(text="O'zbek tili",callback_data='👍uz'),
         InlineKeyboardButton(text="English",callback_data='👍en')]

    ]
)