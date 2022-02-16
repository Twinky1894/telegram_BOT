import json, string, time
from aiogram import types, Dispatcher
from start_bot import dp,bot
from handlers import client

async def stop_words(message : types.Message):
    if{i.lower().translate(str.maketrans('','',string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('stopwords.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()


def register_handlers_common(dp : Dispatcher):
    dp.register_message_handler(stop_words)