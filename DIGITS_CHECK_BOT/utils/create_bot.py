from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import configparser

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
token = config['BOT']['BOT_TOKEN_MAIN']

storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot=bot, storage=storage)
