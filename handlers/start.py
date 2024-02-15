# handlers/start.py
import logging

from aiogram import types

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.book_rooom import button_sequence
from bot import dp, bot  # Keep only dp



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    logging.info("Starting the bot...")
    keyboard_markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton("Найти преподавателя", callback_data='find_teacher'),
        InlineKeyboardButton("Найти кабинет группы", callback_data='find_group_room'),
        InlineKeyboardButton("Узнать информацию о кабинетах", callback_data='room_info'),
        InlineKeyboardButton("Забронировать кабинет", callback_data='book_room'),
        InlineKeyboardButton("Отмена бронирования", callback_data='cancel_book'),
    ]
    keyboard_markup.add(*buttons)

    await message.answer("Выберите действие:", reply_markup=keyboard_markup)
    button_sequence.clear()
    button_sequence.append('miigaik')



@dp.message_handler(commands=['help'])
async def process_start_commanded(message: types.Message):
    technical_support = f"Техническая поддержка: @Vadim_322"
    await bot.send_message(message.chat.id, technical_support)

