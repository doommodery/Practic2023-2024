# handlers/utils.py
import re
from aiogram.types import CallbackQuery, callback_query
from aiogram.types import InlineKeyboardMarkup
from aiogram.types.inline_keyboard import InlineKeyboardButton


async def show_back_button(bot, user_id, chat_id, message_id):
    keyboard_markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
    ]
    keyboard_markup.add(*buttons)

    await bot.send_message(user_id, "Выберите действие:", reply_markup=keyboard_markup)


def validate_user_input(user_input):
    pattern = re.compile(r'\d{4}-(ФГиИБ|ФУТ|ФОП|ФАиГ|КФ|ГФ)-[А-Яа-яA-Za-z]+-\d+[А-Яа-яA-Za-z]*\d*$')

    return bool(pattern)


def validate_user_inputt(user_input):
    pattern = re.compile(r'^\d{3}(к\.2)$')
    return bool(re.match(pattern, user_input))
