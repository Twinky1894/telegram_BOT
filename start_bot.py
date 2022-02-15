import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)