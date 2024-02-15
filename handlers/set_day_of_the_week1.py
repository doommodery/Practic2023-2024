
from aiogram import types
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from bot import bot
from handlers.book_rooom import button_sequence

from handlers.utils import show_back_button


async def set_day_of_the_week1_callback(callback_query: CallbackQuery):
    button_sequence.append(callback_query.data)
    await show_day_of_the_week1_keyboard(callback_query.from_user.id, callback_query.message.message_id)


async def show_day_of_the_week1_keyboard(user_id, message_id=None):
    keyboard_markup = InlineKeyboardMarkup(row_width=2)
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
    buttons = [InlineKeyboardButton(day, callback_data=f'{day}') for day in days]
    buttons.append(InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'))
    keyboard_markup.add(*buttons)
    await bot.edit_message_text(chat_id=user_id, message_id=message_id, text="Выберите день недели:",
                                reply_markup=keyboard_markup)

