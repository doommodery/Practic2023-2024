
from aiogram import types
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from bot import bot
from handlers.book_rooom import button_sequence

from handlers.utils import show_back_button


async def set_floor2_callback(callback_query: CallbackQuery):
    #await show_building_keyboard(callback_query.from_user.id, callback_query.message.message_id)
    button_sequence.append(callback_query.data)
    action = callback_query.data

    if action == '2Body':
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        buttons = [
            InlineKeyboardButton("1 этаж", callback_data='1Floor'),
            InlineKeyboardButton("3 этаж", callback_data='3Floor'),
            InlineKeyboardButton("5 этаж", callback_data='5Floor'),
            InlineKeyboardButton("6 этаж", callback_data='6Floor'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                text="Выберите этаж:",
                                reply_markup=keyboard_markup)


#async def show_building_keyboard(user_id, message_id=None):
    #keyboard_markup = InlineKeyboardMarkup(row_width=2)
    #days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
    #buttons = [InlineKeyboardButton(day, callback_data=f'set_day_{day}') for day in days]
    #buttons.append(InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'))
    #keyboard_markup.add(*buttons)
    #await bot.send_message(user_id, "Выберите день недели:", reply_markup=keyboard_markup)
