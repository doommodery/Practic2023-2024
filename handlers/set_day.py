
from aiogram import types
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from bot import bot
from handlers.book_rooom import button_sequence

from handlers.utils import show_back_button


async def set_building_2_call(callback_query: CallbackQuery):
    button_sequence.append(callback_query.data)
    await show_floor_2_keyboard(callback_query.from_user.id, callback_query.message.message_id)


async def show_floor_2_keyboard(user_id, message_id=None):
    keyboard_markup = InlineKeyboardMarkup(row_width=3)
    buttons = [
        InlineKeyboardButton("1 пара", callback_data='1pair'),
        InlineKeyboardButton("2 пара", callback_data='2pair'),
        InlineKeyboardButton("3 пара", callback_data='3pair'),
        InlineKeyboardButton("4 пара", callback_data='4pair'),
        InlineKeyboardButton("5 пара", callback_data='5pair'),
        InlineKeyboardButton("6 пара", callback_data='6pair'),
        InlineKeyboardButton("7 пара", callback_data='7pair'),
        InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
    ]
    keyboard_markup.add(*buttons)
    await bot.edit_message_text(chat_id=user_id, message_id=message_id, text="Выберите академический час:",
                                reply_markup=keyboard_markup)

    print(button_sequence)