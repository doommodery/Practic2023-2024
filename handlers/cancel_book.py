import os
import json
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def has_booking(user_id):
    file_path = os.path.join(os.path.expanduser(f"C:/Users/Vadim/OneDrive/Рабочий стол/{user_id}_bookings.txt"))

    if not os.path.exists(file_path):
        return False  # Файл не найден

    with open(file_path, "r", encoding='utf-8') as file:
        for line in file:
            try:
                values_list = json.loads(line.replace("'", '"'))
            except ValueError:
                return False  # Ошибка при чтении файла

            if values_list[0] == 'miigaik':
                return True

    return False

async def process_booking_data(user_id):
    file_path = os.path.join(os.path.expanduser(f"C:/Users/Vadim/OneDrive/Рабочий стол/{user_id}_bookings.txt"))

    if not os.path.exists(file_path):
        return None  # Файл не найден

    buttons = []

    with open(file_path, "r", encoding='utf-8') as file:
        for line in file:
            try:
                values_list = json.loads(line.replace("'", '"'))
            except ValueError:
                return None  # Ошибка при чтении файла

            formatted_values = []
            for value in values_list[1:]:
                if value.endswith('Body'):
                    formatted_values.append(f"{value[0]} корпус")
                elif value.endswith('Floor'):
                    formatted_values.append(f"{value[0]} этаж")
                elif value.endswith('к.1'):
                    formatted_values.append(value[:-2])
                elif value.endswith('pair'):
                    formatted_values.append(f"{value[0]} пара")
                else:
                    formatted_values.append(value)

            processed_data = '\n'.join(formatted_values)
            button = InlineKeyboardButton(text=processed_data, callback_data='booking_info')
            buttons.append(button)

    return_buttons = [
        InlineKeyboardButton("Вернуться в главное меню", callback_data='back_to_start'),
    ]

    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons, *return_buttons)

    return keyboard

async def create_inline_button(user_id):
    processed_data = await process_booking_data(user_id)

    if processed_data is not None:
        print(processed_data)
        return processed_data

    return None