from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards import kb_client


# @dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Приятного аппетита", reply_markup=kb_client)
    except:
        await message.reply("Общение с ботом через ЛС")


# @dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await message.reply("ПН-ВС с 9:00 до 18:00!")


# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await message.reply("Улица Пушкина, дом Колотушкина")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
