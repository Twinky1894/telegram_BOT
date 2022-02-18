import json, string, time
from aiogram.utils import executor
from start_bot import dp
from handlers import client, admin, common
    
async def on_startup(_):
    print('Бот вышел в сеть')

client.register_handlers_client(dp)

common.register_handlers_common(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
