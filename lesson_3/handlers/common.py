from aiogram import types, F, Router
from aiogram.filters.command import Command
import logging
import random
from keyboards.keyboards import kb1, kb2
from utils.random_gif import gif

router = Router()

# Хэндлер на команду /start
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer (f'Привет, {name}', reply_markup=kb1)
    # await message.answer ('Привет, ', name)

# Хэндлер на команду /stop
@router.message(Command('stop'))
@router.message(Command('стоп'))
async def cmd_stop(message: types.Message):
    await message.answer (f'До свидания, {message.chat.first_name}')
    await router.stop_polling()

# Хэндлер на команду /gif
@router.message(Command('gif'))
@router.message(Command('картинка'))
@router.message(F.text.lower() == 'покажи картинку') 
async def cmd_gif(message: types.Message):
    name = message.chat.first_name
    img_gif = gif()
    await message.answer (f'Лови картинку, {message.chat.first_name}')   
    await message.answer_photo (photo = img_gif)
    # await bot.send_photo(message.from_user.id, photo = img_cat)  

# Хэндлер на сообщения
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user: 
        await message.answer (f'Привет, {name}')
    elif 'пока' == msg_user: 
        await message.answer (f'Пока, {name}')
    elif 'кости' in msg_user: 
        await message.answer_dice (emoji="🎲")
    elif 'картинка' in msg_user: 
        await message.answer (f'Смотри, {name}')      
    else:
        await message.answer('Я не знаю такого слова')          
