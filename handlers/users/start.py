from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart,CallbackQuery
from api import create_user,change,get_image
from loader import dp
from aiogram.dispatcher.filters import Text
from keyboards.inline.button import btn
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    create_user(message.from_user.full_name,message.from_user.id)
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\n"
                         f"Tilni tanlang!",reply_markup=btn)
@dp.callback_query_handler(Text(startswith='👍'))
async def get_language(call:CallbackQuery):
    til = call.data
    til = til[1:]
    change(call.from_user.id,til)
    await call.answer(cache_time=60)
    if til=='uz':
        await call.message.answer('Til ozgardi')
    else:
        await call.message.answer("Language changed")
    await call.message.delete()
@dp.message_handler(commands='image')
async def image(message:types.Message):
    images = get_image()
    for image in images:
        await message.answer_photo(photo=image)
