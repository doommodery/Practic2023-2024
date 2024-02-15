# handlers/help.py
from aiogram import types
from main import dp, bot

@dp.message_handler(commands=['help'])
async def process_start_commanded(message: types.Message):
    technical_support = f"Техническая поддержка: @Vadim_322"
    await bot.send_message(message.chat.id, technical_support)
