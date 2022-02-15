import json, string
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup
from start_bot import dp
from handlers import client, admin, common

#

#b5 = KeyboardButton('Вернуться в главное меню')
#kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
#kb_menu.add(b5)
    
async def on_startup(_):
    print('Бот вышел в сеть')

client.register_handlers_client(dp)

common.register_handlers_common(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

#⚒Некоторые дефекты можно устранить самостоятельно, без обращения в сервис , это поможет вам сэкономить время.\n\n📔Следуя простым инструкциям вы сможете провести настройку или обслуживание вашего устройства, для восстановления его работоспособности.