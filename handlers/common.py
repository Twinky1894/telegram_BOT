import json, string, time
from aiogram import types, Dispatcher
from start_bot import dp,bot
from handlers import client
from keyboards import kb_start

async def stop_words(message : types.Message):
    if{i.lower().translate(str.maketrans('','',string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('stopwords.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()
    else: await message.reply('Я не совсем понял что вы имели ввиду. Для того чтобы отпраить нам сообщение по вопросу ремонта вашего устройства, воспользуйтесь кнопкой "Консультация". Если хотите оставить обратную связь по работе сервисного центра, либо сталкнулись с какой то проблемой, воспользуйтесь кнопкой "Обратная связь", либо перезапустите бота командой /start и попробуйте снова', reply_markup=kb_start)

def register_handlers_common(dp : Dispatcher):
    dp.register_message_handler(stop_words)