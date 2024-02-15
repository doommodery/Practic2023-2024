import logging
import re

from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, callback_query
import json


async def info(bot, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    action = callback_query.data
    print(action)
    if action.startswith('room'):
        room_number = str(action.split('_')[-1])
        with open("1.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
        for body in data.values():
            for floor in data["miigaik"].values():
                # Проверяем наличие первого этажа "1Floor"
                if "1Floor" in floor:
                    # Проверяем наличие аудитории на этаже
                    if room_number in floor["1Floor"]:
                        json_fil = floor["1Floor"][room_number]
                        for abc in json_fil:
                            message_text = f"Информация о кабинете номер {abc['room']} - Размер: {abc['syze']} - Доступ к Wi-Fi: {abc['Access_WIFI']} - Количество компьютеров: {abc['Computers']} - Тип доски: {abc['desks']} - Наличие проектора: {abc['projectors']}"
                            await bot.send_message(user_id, message_text)
                            return
            for floor, rooms in body.items():
                if room_number in rooms:
                    json_fil = rooms[room_number]
                    for abc in json_fil:
                        message_text = f"Информация о кабинете номер {abc['room']} - Размер: {abc['syze']} - Доступ к Wi-Fi: {abc['Access_WIFI']} - Количество компьютеров: {abc['Computers']} - Тип доски: {abc['desks']} - Наличие проектора: {abc['projectors']}"
                        await bot.send_message(user_id, message_text)
                        return


async def get_room_info(bot, user_id, user_input, waiting_for_room, callback_query: CallbackQuery):
    pattern = re.compile(r'^\d{3}(к\.2)?$')
    if bool(re.match(pattern, user_input)):
        room_number = str(user_input)
        with open("1.json", 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Проверяем наличие корпуса "miigaik"
        for body in data.values():
            for floor in data["miigaik"].values():
                # Проверяем наличие первого этажа "1Floor"
                if "1Floor" in floor:
                    # Проверяем наличие аудитории на этаже
                    if room_number in floor["1Floor"]:
                        json_fil = floor["1Floor"][room_number]
                        for abc in json_fil:
                            message_text = f"Информация о кабинете номер {abc['room']} - Размер: {abc['syze']} - Доступ к Wi-Fi: {abc['Access_WIFI']} - Количество компьютеров: {abc['Computers']} - Тип доски: {abc['desks']} - Наличие проектора: {abc['projectors']}"
                            await bot.send_message(user_id, message_text)
                            return False  # Найдена аудитория, завершаем ожидание
            for floor, rooms in body.items():
                if room_number in rooms:
                    json_fil = rooms[room_number]
                    for abc in json_fil:
                        message_text = f"Информация о кабинете номер {abc['room']} - Размер: {abc['syze']} - Доступ к Wi-Fi: {abc['Access_WIFI']} - Количество компьютеров: {abc['Computers']} - Тип доски: {abc['desks']} - Наличие проектора: {abc['projectors']}"
                        await bot.send_message(user_id, message_text)
                        return False  # Найдена аудитория, завершаем ожидание

        # Если не найдено ни на одном этаже, сообщаем об этом
        await bot.send_message(user_id,
                               "Аудитория не найдена в базе данных. Пожалуйста, введите номер существующей аудитории")
        return waiting_for_room

    else:
        await bot.send_message(user_id,
                               "Неверный формат ввода. Пожалуйста, введите корректный номер аудитории")
        return waiting_for_room

        # Проверяем, существует ли указанный университет и здание в JSON-файле
        # if university in data and building in data[university]:
        # Проверяем, существует ли указанный этаж в JSON-файле
        # if floor in data[university][building]:
        # Проверяем, существует ли указанный кабинет в JSON-файле
        # if room_numbery in data[university][building][floor]:
        # if room_numbery['room'] == room_numbery:
        # Формируем сообщение с информацией и отправляем пользователю
        # message_text = f"Информация о кабинете {room_number}:\n\n"
        # message_text += f"Размер: {room_numbery['syze']}\n"
        # message_text += f"Доступ к Wi-Fi: {room_numbery['Access_WIFI']}\n"
        # message_text += f"Количество компьютеров: {room_numbery['Computers']}\n"
        # message_text += f"Столы: {room_numbery['desks']}\n"
        # message_text += f"Проектор: {room_numbery['projectors']}\n"
        # return message_text

        # Если кабинет не найден, возвращаем None
        # print(f"кабинет {room_number} не найден.")
        # return None

    # except FileNotFoundError:
    # Если файл не найден, выводим сообщение об ошибке
    # print(f"Файл {json_file_path} не найден.")
    # return None
    # except Exception as e:
    # Обрабатываем другие ошибки
    # print(f"Произошла ошибка: {str(e)}")
    # return None
