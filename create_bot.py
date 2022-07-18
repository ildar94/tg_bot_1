from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token="5417793025:AAE3GU-TFsev7BAD8ARqkua36zSyIOo8BN8")
dp = Dispatcher(bot, storage=storage)

