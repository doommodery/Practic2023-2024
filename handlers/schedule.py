import json

import requests
import datetime
import types
import urllib.request
from aiogram.types import callback_query

# from handlers.callbacks import endpoint

from handlers.utils import validate_user_input

tek_data = datetime.datetime.now()
nomer_dnya = tek_data.weekday()

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
b = "нижняя"


async def of_the_week(bot, callback_query, endpoint):
    user_id = callback_query.from_user.id
    action = callback_query.data
    base_url = 'https://study.miigaik.ru/api/v1/'
    url = f'{base_url}{endpoint}'
    response = requests.get(url, verify=False)
    data = response.json()
    if action == 'today':
        monday_schedule = data[b][days[nomer_dnya]]  # Get the schedule for Monday
        if monday_schedule:
            for lesson_info in monday_schedule:
                lesson_text = f"{days[nomer_dnya]}: {lesson_info['lesson']} - {lesson_info['subject']} - {lesson_info['teacher']} - {lesson_info['classroom']}"
                await bot.send_message(user_id, lesson_text)
        else:
            await bot.send_message(user_id, "На сегодня занятий нет.")
    elif action == 'monday':
        monday_schedule = data[b][days[0]]  # Get the schedule for Monday
        if monday_schedule:
            for lesson_info in monday_schedule:
                lesson_text = f"Понедельник: {lesson_info['lesson']} - {lesson_info['subject']} - {lesson_info['teacher']} - {lesson_info['classroom']}"
                await bot.send_message(user_id, lesson_text)
        else:
            await bot.send_message(user_id, "На понедельник занятий нет.")
    elif action == 'tuesday':
        monday_schedule = data[b][days[1]]  # Get the schedule for Monday
        if monday_schedule:
            for lesson_info in monday_schedule:
                lesson_text = f"Вторник: {lesson_info['lesson']} - {lesson_info['subject']} - {lesson_info['teacher']} - {lesson_info['classroom']}"
                await bot.send_message(user_id, lesson_text)
        else:
            await bot.send_message(user_id, "На вторник занятий нет.")
    elif action == 'wednesday':
        monday_schedule = data[b][days[2]]  # Get the schedule for Monday
        if monday_schedule:
            for lesson_info in monday_schedule:
                lesson_text = f"Среда: {lesson_info['lesson']} - {lesson_info['subject']} - {lesson_info['teacher']} - {lesson_info['classroom']}"
                await bot.send_message(user_id, lesson_text)
        else:
            await bot.send_message(user_id, "На среду занятий нет.")
    elif action == 'thursday':
        monday_schedule = data[b][days[3]]  # Get the schedule for Monday
        if monday_schedule:
            for lesson_info in monday_schedule:
                lesson_text = f"Четверг: {lesson_info['lesson']} - {lesson_info['subject']} - {lesson_info['teacher']} - {lesson_info['classroom']}"
                await bot.send_message(user_id, lesson_text)
        else:
            await bot.send_message(user_id, "На четверг занятий нет.")
    elif action == 'friday':
        monday_schedule = data[b][days[4]]  # Get the schedule for Monday
        if monday_schedule:
            for lesson_info in monday_schedule:
                lesson_text = f"Пятница: {lesson_info['lesson']} - {lesson_info['subject']} - {lesson_info['teacher']} - {lesson_info['classroom']}"
                await bot.send_message(user_id, lesson_text)
        else:
            await bot.send_message(user_id, "На пятницу занятий нет.")
    else:
        monday_schedule = data[b][days[5]]  # Get the schedule for Monday
        if monday_schedule:
            for lesson_info in monday_schedule:
                lesson_text = f"Суббота: {lesson_info['lesson']} - {lesson_info['subject']} - {lesson_info['teacher']} - {lesson_info['classroom']}"
                await bot.send_message(user_id, lesson_text)
        else:
            await bot.send_message(user_id, "На субботу занятий нет.")
