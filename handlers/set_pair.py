# set_pair.py
from aiogram import types
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from bot import bot

from handlers.utils import show_back_button


async def set_pair_callback(callback_query: CallbackQuery):
    #button_sequence.append(callback_query.data)
    await show_filter_keyboard(callback_query.from_user.id, callback_query.message.message_id)


async def show_filter_keyboard(user_id, message_id=None):
    # логика обработки set_pair
    keyboard_markup = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton("Нажми сюда", callback_data='filter'),
        InlineKeyboardButton("Вернуться назад", callback_data='back_to_start')
    ]
    keyboard_markup.add(*buttons)
    await bot.edit_message_text(chat_id=user_id, message_id=message_id, text="Выберите фильтр:",
                                reply_markup=keyboard_markup)
