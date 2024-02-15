from aiogram import types
# from aiogram.handlers import callback_query

from aiogram.types import CallbackQuery, message_id
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot import bot  # Проверьте, что путь к bot.py корректен
from handlers.utils import show_back_button
global button_sequence

button_sequence = ["miigaik"]



async def book_room_callback(callback_query: CallbackQuery):
    # Ваша логика обработки book_room

    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    await show_days_keyboard(callback_query.from_user.id)


async def show_days_keyboard(user_id):
    keyboard_markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton("1 корпус", callback_data='1Body'),
        InlineKeyboardButton("2 корпус", callback_data='2Body'),
        InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
    ]
    keyboard_markup.add(*buttons)
    await bot.send_message(user_id, "Выберите корпус:", reply_markup=keyboard_markup)
