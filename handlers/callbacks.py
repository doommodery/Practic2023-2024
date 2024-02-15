# handlers/callbacks.py
import json
import re

import types
from aiogram import types
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, callback_query
from aiogram.types import Message
from bot import dp, bot  # Import inside the handler function
from handlers.book_rooom import book_room_callback, button_sequence, show_days_keyboard
from handlers.cancel_book import create_inline_button, process_booking_data, has_booking
from handlers.deleting_a_reservation import deleting_a_reservation
# from handlers.cancel_book import cancel_book_callback
from handlers.info_auditorium import get_room_info, info
from handlers.reservation_room import find_and_flatten_unbooking_pairs
from handlers.set_day_of_the_week2 import set_day_of_the_week2_callback
from handlers.set_floor1 import set_floor1_callback
from handlers.set_day_of_the_week1 import set_day_of_the_week1_callback
from handlers.Automatic_buttons import send_buttons
from handlers.set_floor2 import set_floor2_callback
from handlers.start import process_start_command
from handlers.utils import show_back_button, validate_user_input, validate_user_inputt
# from main import selected_options
from handlers.schedule import of_the_week
from handlers.book_rooom import book_room_callback
from handlers.change_of_booking_status import booking_status
waiting_for_group = False
waiting_for_room = False
json_file = 'Groups.json'



@dp.callback_query_handler(lambda callback_query: callback_query.data == 'book_room')
async def process_book_room(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id

    if await has_booking(user_id):
        await bot.delete_message(chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id)
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        buttons = [
            InlineKeyboardButton("Вернуться в главное меню", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.send_message(user_id, text = "У вас уже есть забронированная аудитория. Больше одной - нельзя!", reply_markup = keyboard_markup)
    else:
        await bot.delete_message(chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id)
        await show_days_keyboard(user_id)

# @dp.callback_query_handler(lambda callback_query: callback_query.data == 'cancel_book')
# async def process_cancel_book(callback_query: CallbackQuery):
# await cancel_book_callback(callback_query.from_user.id, bot)

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('1Body'))
async def process_set_floor1(callback_query: CallbackQuery):
    await set_floor1_callback(callback_query)


@dp.callback_query_handler(lambda callback_query: callback_query.data.endswith('Floorr'))
async def process_set_auditorium1(callback_query: CallbackQuery):
    action = callback_query.data
    if action == '1Floorr':
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        buttons = [
            InlineKeyboardButton("154", callback_data='154к.1'),
            InlineKeyboardButton("165", callback_data='165к.1'),
            InlineKeyboardButton("166", callback_data='166к.1'),
            InlineKeyboardButton("170", callback_data='170к.1'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите аудиторию:",
                                    reply_markup=keyboard_markup)
        button_sequence.append(callback_query.data[:-1])

    elif action == '4Floorr':
        keyboard_markup = InlineKeyboardMarkup(row_width=4)
        buttons = [
            InlineKeyboardButton("401", callback_data='401к.1'),
            InlineKeyboardButton("402", callback_data='402к.1'),
            InlineKeyboardButton("403", callback_data='403к.1'),
            InlineKeyboardButton("404", callback_data='404к.1'),
            InlineKeyboardButton("406", callback_data='406к.1'),
            InlineKeyboardButton("409", callback_data='409к.1'),
            InlineKeyboardButton("410", callback_data='410к.1'),
            InlineKeyboardButton("410б", callback_data='410бк.1'),
            InlineKeyboardButton("411", callback_data='411к.1'),
            InlineKeyboardButton("414", callback_data='414к.1'),
            InlineKeyboardButton("420", callback_data='420к.1'),
            InlineKeyboardButton("423", callback_data='423к.1'),
            InlineKeyboardButton("423б", callback_data='423бк.1'),
            InlineKeyboardButton("424", callback_data='424к.1'),
            InlineKeyboardButton("425", callback_data='425к.1'),
            InlineKeyboardButton("426", callback_data='426к.1'),
            InlineKeyboardButton("434а", callback_data='434ак.1'),
            InlineKeyboardButton("434б", callback_data='434бк.1'),
            InlineKeyboardButton("450", callback_data='450к.1'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите аудиторию:",
                                    reply_markup=keyboard_markup)
        button_sequence.append(callback_query.data[:-1])
    elif action == '5Floorr':
        keyboard_markup = InlineKeyboardMarkup(row_width=4)
        buttons = [
            InlineKeyboardButton("503", callback_data='503к.1'),
            InlineKeyboardButton("506", callback_data='506к.1'),
            InlineKeyboardButton("507", callback_data='507к.1'),
            InlineKeyboardButton("513", callback_data='513к.1'),
            InlineKeyboardButton("514", callback_data='514к.1'),
            InlineKeyboardButton("515", callback_data='515к.1'),
            InlineKeyboardButton("516", callback_data='516к.1'),
            InlineKeyboardButton("519", callback_data='519к.1'),
            InlineKeyboardButton("520", callback_data='520к.1'),
            InlineKeyboardButton("550", callback_data='550к.1'),
            InlineKeyboardButton("554", callback_data='554к.1'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите аудиторию:",
                                    reply_markup=keyboard_markup)
        button_sequence.append(callback_query.data[:-1])
    elif action == '6Floorr':
        keyboard_markup = InlineKeyboardMarkup(row_width=4)
        buttons = [
            InlineKeyboardButton("601", callback_data='601к.1'),
            InlineKeyboardButton("602", callback_data='602к.1'),
            InlineKeyboardButton("603", callback_data='603к.1'),
            InlineKeyboardButton("604", callback_data='604к.1'),
            InlineKeyboardButton("605", callback_data='605к.1'),
            InlineKeyboardButton("606", callback_data='606к.1'),
            InlineKeyboardButton("607", callback_data='607к.1'),
            InlineKeyboardButton("608", callback_data='608к.1'),
            InlineKeyboardButton("609", callback_data='609к.1'),
            InlineKeyboardButton("621", callback_data='621к.1'),
            InlineKeyboardButton("622а", callback_data='622ак.1'),
            InlineKeyboardButton("622б", callback_data='622бк.1'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите аудиторию:",
                                    reply_markup=keyboard_markup)
        button_sequence.append(callback_query.data[:-1])


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('2Body'))
async def process_set_floor2(callback_query: CallbackQuery):
    await set_floor2_callback(callback_query)


@dp.callback_query_handler(lambda callback_query: callback_query.data.endswith('Floor'))
async def process_set_auditorium2(callback_query: CallbackQuery):
    action = callback_query.data
    if action == '1Floor':
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        buttons = [
            InlineKeyboardButton("101к.2", callback_data='101к.2'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)

        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите аудиторию:",
                                    reply_markup=keyboard_markup)
        button_sequence.append(callback_query.data)
    elif action == '3Floor':
        keyboard_markup = InlineKeyboardMarkup(row_width=3)
        buttons = [
            InlineKeyboardButton("302к.2", callback_data='302к.2'),
            InlineKeyboardButton("303к.2", callback_data='303к.2'),
            InlineKeyboardButton("304к.2", callback_data='304к.2'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)

        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите аудиторию:",
                                    reply_markup=keyboard_markup)
        button_sequence.append(callback_query.data)
    elif action == '5Floor':
        keyboard_markup = InlineKeyboardMarkup(row_width=4)
        buttons = [
            InlineKeyboardButton("507к.2", callback_data='507к.2'),
            InlineKeyboardButton("508к.2", callback_data='508к.2'),
            InlineKeyboardButton("509к.2", callback_data='509к.2'),
            InlineKeyboardButton("510к.2", callback_data='510к.2'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите аудиторию:",
                                    reply_markup=keyboard_markup)
        button_sequence.append(callback_query.data)
    elif action == '6Floor':
        keyboard_markup = InlineKeyboardMarkup(row_width=4)
        buttons = [
            InlineKeyboardButton("601к.2", callback_data='601к.2'),
            InlineKeyboardButton("602к.2", callback_data='602к.2'),
            InlineKeyboardButton("603к.2", callback_data='603к.2'),
            InlineKeyboardButton("604к.2", callback_data='604к.2'),
            InlineKeyboardButton("605к.2", callback_data='605к.2'),
            InlineKeyboardButton("606к.2", callback_data='606к.2'),
            InlineKeyboardButton("607к.2", callback_data='607к.2'),
            InlineKeyboardButton("608к.2", callback_data='608к.2'),
            InlineKeyboardButton("609к.2", callback_data='609к.2'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите аудиторию:",
                                    reply_markup=keyboard_markup)
        button_sequence.append(callback_query.data)


@dp.callback_query_handler(lambda callback_query: callback_query.data.endswith('к.2'))
async def process_set_day_of_the_week2(callback_query: CallbackQuery):
    await set_day_of_the_week2_callback(callback_query)


@dp.callback_query_handler(lambda callback_query: callback_query.data.endswith('к.1'))
async def process_set_day_of_the_week1(callback_query: CallbackQuery):
    await set_day_of_the_week1_callback(callback_query)


@dp.callback_query_handler(
    lambda callback_query: callback_query.data in ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'])
async def process_set_pair(callback_query: CallbackQuery):
    json_file_path = 'booking_down.json'
    result_list = find_and_flatten_unbooking_pairs(callback_query, json_file_path)
    print(result_list)
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    await send_buttons(callback_query.from_user.id, bot, result_list)
    # await bot.send_message(callback_query.from_user.id, result_list)


@dp.callback_query_handler(lambda callback_query: callback_query.data.endswith('pair'))
async def process_schange_of_booking_status(callback_query: CallbackQuery):
    print('сработа функция с джейсоном')
    await booking_status(callback_query, callback_query.from_user.id)
    keyboard_markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton("Вернуться в главное меню", callback_data='back_to_start'),
    ]
    keyboard_markup.add(*buttons)
    await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                text="Аудитория забронирована!", reply_markup=keyboard_markup)
    button_sequence = ["miigaik"]


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'booking_info')
async def process_deleting_a_reservation(callback_query: CallbackQuery):
    aaa = await deleting_a_reservation(callback_query.from_user.id)
    print(aaa)
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    keyboard_markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton("Вернуться в главное меню", callback_data='back_to_start'),
    ]
    keyboard_markup.add(*buttons)
    await bot.send_message(callback_query.from_user.id, aaa, reply_markup=keyboard_markup)

@dp.callback_query_handler(lambda callback_query: callback_query.data == 'cancel_book')
async def process_create_inline_button(callback_query: CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    keyboard = await create_inline_button(callback_query.from_user.id)

    if keyboard is not None:
        await bot.send_message(chat_id=callback_query.from_user.id, text="Информация о бронировании (Чтобы отменить бронирование нажмите на кнопку с соответствующей аудиторией):",
                               reply_markup=keyboard)
    else:
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        buttons = [
            InlineKeyboardButton("Вернуться в главное меню", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.send_message(chat_id=callback_query.from_user.id,text="У вас нет забронированных аудиторий.",reply_markup=keyboard_markup)


# @dp.callback_query_handler(lambda callback_query: callback_query.data in ['1pair', '2pair', '3pair', '4pair', '5pair', '6pair', '7pair'])
# async def process_set_building(callback_query: CallbackQuery):
# await bot.delete_message(chat_id=callback_query.message.chat.id,
# message_id=callback_query.message.message_id)
# await reservation(bot, callback_query, callback_query.from_user.id)


@dp.callback_query_handler(lambda callback_query: True)
async def process_callback(callback_query: CallbackQuery):
    action = callback_query.data
    global waiting_for_group
    global waiting_for_room

    if action == 'find_teacher':
        await bot.send_message(callback_query.from_user.id, "Выбрано: Найти преподавателя")
        await bot.delete_message(chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id)
        await show_back_button(bot, callback_query.from_user.id, callback_query.message.chat.id,
                               callback_query.message.message_id)


    elif action == 'find_group_room':
        await bot.send_message(callback_query.from_user.id,
                               "Напишите учебную группу, формат: ГГГГ-ФАК-СПЕЦ-ГРУППА, пример: 2021-ФГиИБ-ПИ-1б")
        await bot.delete_message(chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id)
        waiting_for_group = True
        waiting_for_room = False

    elif action == 'room_info':
        await bot.send_message(callback_query.from_user.id,
                               "Выберите аудиторию или введите её номер, пример ввода: 101 - для первого корпуса, 101к.2 - для второго корпуса")
        waiting_for_room = True
        waiting_for_group = False
        await bot.delete_message(chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id)
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        buttons = [
            InlineKeyboardButton("1 корпус", callback_data='building_1'),
            InlineKeyboardButton("2 корпус", callback_data='building_2'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.send_message(callback_query.from_user.id, "Выберите корпус:", reply_markup=keyboard_markup)

    elif action == 'building_1':
        keyboard_markup = InlineKeyboardMarkup(row_width=3)
        buttons = [
            InlineKeyboardButton("1 этаж", callback_data='Floor_1_1'),
            InlineKeyboardButton("2 этаж", callback_data='Floor_1_2'),
            InlineKeyboardButton("3 этаж", callback_data='Floor_1_3'),
            InlineKeyboardButton("4 этаж", callback_data='Floor_1_4'),
            InlineKeyboardButton("5 этаж", callback_data='Floor_1_5'),
            InlineKeyboardButton("6 этаж", callback_data='Floor_1_6'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите этаж:",
                                    reply_markup=keyboard_markup)
        waiting_for_room = False

    elif action == 'building_2':
        keyboard_markup = InlineKeyboardMarkup(row_width=3)
        buttons = [
            InlineKeyboardButton("1 этаж", callback_data='Floor_2_1'),
            InlineKeyboardButton("2 этаж", callback_data='Floor_2_2'),
            InlineKeyboardButton("3 этаж", callback_data='Floor_2_3'),
            InlineKeyboardButton("4 этаж", callback_data='Floor_2_4'),
            InlineKeyboardButton("5 этаж", callback_data='Floor_2_5'),
            InlineKeyboardButton("6 этаж", callback_data='Floor_2_6'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите этаж:",
                                    reply_markup=keyboard_markup)
        waiting_for_room = False

    elif action == 'Floor_1_1':
        keyboard_markup = InlineKeyboardMarkup(row_width=2)
        buttons = [
            InlineKeyboardButton("154", callback_data='room_1_1_154'),
            InlineKeyboardButton("165", callback_data='room_1_1_165'),
            InlineKeyboardButton("166", callback_data='room_1_1_166'),
            InlineKeyboardButton("170", callback_data='room_1_1_170'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите аудиторию:",
                                    reply_markup=keyboard_markup)

    elif action == 'Floor_1_2':
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        buttons = [
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Нет информации о аудиториях на данном этаже",
                                    reply_markup=keyboard_markup)

    elif action == 'Floor_1_3':
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        buttons = [
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Нет информации о аудиториях на данном этаже",
                                    reply_markup=keyboard_markup)

    elif action == 'Floor_1_4':
        keyboard_markup = InlineKeyboardMarkup(row_width=4)
        buttons = [
            InlineKeyboardButton("401", callback_data='room_1_4_401'),
            InlineKeyboardButton("402", callback_data='room_1_4_402'),
            InlineKeyboardButton("403", callback_data='room_1_4_403'),
            InlineKeyboardButton("404", callback_data='room_1_4_404'),
            InlineKeyboardButton("406", callback_data='room_1_4_406'),
            InlineKeyboardButton("409", callback_data='room_1_4_409'),
            InlineKeyboardButton("410", callback_data='room_1_4_410'),
            InlineKeyboardButton("410б", callback_data='room_1_4_410б'),
            InlineKeyboardButton("411", callback_data='room_1_4_411'),
            InlineKeyboardButton("414", callback_data='room_1_4_414'),
            InlineKeyboardButton("420", callback_data='room_1_4_420'),
            InlineKeyboardButton("423", callback_data='room_1_4_423'),
            InlineKeyboardButton("423б", callback_data='room_1_4_423б'),
            InlineKeyboardButton("424", callback_data='room_1_4_424'),
            InlineKeyboardButton("425", callback_data='room_1_4_425'),
            InlineKeyboardButton("426", callback_data='room_1_4_426'),
            InlineKeyboardButton("434а", callback_data='room_1_4_434а'),
            InlineKeyboardButton("434б", callback_data='room_1_4_434б'),
            InlineKeyboardButton("450", callback_data='room_1_4_450'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите аудиторию:",
                                    reply_markup=keyboard_markup)

    elif action == 'Floor_1_5':
        keyboard_markup = InlineKeyboardMarkup(row_width=4)
        buttons = [
            InlineKeyboardButton("503", callback_data='room_1_5_503'),
            InlineKeyboardButton("506", callback_data='room_1_5_506'),
            InlineKeyboardButton("507", callback_data='room_1_5_507'),
            InlineKeyboardButton("513", callback_data='room_1_5_513'),
            InlineKeyboardButton("514", callback_data='room_1_5_514'),
            InlineKeyboardButton("515", callback_data='room_1_5_515'),
            InlineKeyboardButton("516", callback_data='room_1_5_516'),
            InlineKeyboardButton("519", callback_data='room_1_5_519'),
            InlineKeyboardButton("520", callback_data='room_1_5_520'),
            InlineKeyboardButton("550", callback_data='room_1_5_550'),
            InlineKeyboardButton("554", callback_data='room_1_5_554'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите аудиторию:",
                                    reply_markup=keyboard_markup)

    elif action == 'Floor_1_6':
        keyboard_markup = InlineKeyboardMarkup(row_width=4)
        buttons = [
            InlineKeyboardButton("601", callback_data='room_1_6_601'),
            InlineKeyboardButton("602", callback_data='room_1_6_602'),
            InlineKeyboardButton("603", callback_data='room_1_6_603'),
            InlineKeyboardButton("604", callback_data='room_1_6_604'),
            InlineKeyboardButton("605", callback_data='room_1_6_605'),
            InlineKeyboardButton("606", callback_data='room_1_6_606'),
            InlineKeyboardButton("607", callback_data='room_1_6_607'),
            InlineKeyboardButton("608", callback_data='room_1_6_608'),
            InlineKeyboardButton("609", callback_data='room_1_6_609'),
            InlineKeyboardButton("621", callback_data='room_1_6_621'),
            InlineKeyboardButton("622а", callback_data='room_1_6_622а'),
            InlineKeyboardButton("622б", callback_data='room_1_6_622б'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите аудиторию:",
                                    reply_markup=keyboard_markup)

    elif action == 'Floor_2_1':
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        buttons = [
            InlineKeyboardButton("101к.2", callback_data='room_2_1_101к.2'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)

        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите аудиторию:",
                                    reply_markup=keyboard_markup)
    elif action == 'Floor_2_2':
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        buttons = [
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Нет информации о аудиториях на данном этаже",
                                    reply_markup=keyboard_markup)

    elif action == 'Floor_2_3':
        keyboard_markup = InlineKeyboardMarkup(row_width=3)
        buttons = [
            InlineKeyboardButton("302к.2", callback_data='room_2_3_302к.2'),
            InlineKeyboardButton("303к.2", callback_data='room_2_3_303к.2'),
            InlineKeyboardButton("304к.2", callback_data='room_2_3_304к.2'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)

        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите аудиторию:",
                                    reply_markup=keyboard_markup)

    elif action == 'Floor_2_4':
        keyboard_markup = InlineKeyboardMarkup(row_width=1)
        buttons = [
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Нет информации о аудиториях на данном этаже",
                                    reply_markup=keyboard_markup)

    elif action == 'Floor_2_5':
        keyboard_markup = InlineKeyboardMarkup(row_width=4)
        buttons = [
            InlineKeyboardButton("507к.2", callback_data='room_2_5_507к.2'),
            InlineKeyboardButton("508к.2", callback_data='room_2_5_508к.2'),
            InlineKeyboardButton("509к.2", callback_data='room_2_5_509к.2'),
            InlineKeyboardButton("510к.2", callback_data='room_2_5_510к.2'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите аудиторию:",
                                    reply_markup=keyboard_markup)

    elif action == 'Floor_2_6':
        keyboard_markup = InlineKeyboardMarkup(row_width=4)
        buttons = [
            InlineKeyboardButton("601к.2", callback_data='room_2_6_601к.2'),
            InlineKeyboardButton("602к.2", callback_data='room_2_6_602к.2'),
            InlineKeyboardButton("603к.2", callback_data='room_2_6_603к.2'),
            InlineKeyboardButton("604к.2", callback_data='room_2_6_604к.2'),
            InlineKeyboardButton("605к.2", callback_data='room_2_6_605к.2'),
            InlineKeyboardButton("606к.2", callback_data='room_2_6_606к.2'),
            InlineKeyboardButton("607к.2", callback_data='room_2_6_607к.2'),
            InlineKeyboardButton("608к.2", callback_data='room_2_6_608к.2'),
            InlineKeyboardButton("609к.2", callback_data='room_2_6_609к.2'),
            InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
        ]
        keyboard_markup.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Выберите аудиторию:",
                                    reply_markup=keyboard_markup)

    elif action.startswith('room'):
        await info(bot, callback_query)

    elif action in ['today', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        await of_the_week(bot, callback_query, endpoint)

    elif action == 'back_to_start':

        # Возвращаем пользователя к начальному экрану
        await process_start_command(Message(chat=callback_query.message.chat,
                                            from_user=callback_query.from_user))
        await bot.delete_message(chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id)
        waiting_for_group = False
        waiting_for_room = False

@dp.message_handler()
async def handle_text(message: types.Message):
    global waiting_for_group
    global endpoint
    global waiting_for_room
    if waiting_for_group:
        user_input = message.text
        if validate_user_input(user_input):
            with open("Groops.json", "r", encoding="utf-8") as file:
                group_data = json.load(file)
                is_valid_group = user_input in group_data.keys()
                if is_valid_group:
                    endpoint = group_data[user_input]
                    keyboard_markup = InlineKeyboardMarkup(row_width=2)
                    buttons = [
                        InlineKeyboardButton("Сегодня", callback_data='today'),
                        InlineKeyboardButton("Понедельник", callback_data='monday'),
                        InlineKeyboardButton("Вторник", callback_data='tuesday'),
                        InlineKeyboardButton("Среда", callback_data='wednesday'),
                        InlineKeyboardButton("Четверг", callback_data='thursday'),
                        InlineKeyboardButton("Пятница", callback_data='friday'),
                        InlineKeyboardButton("Суббота", callback_data='saturday'),
                        InlineKeyboardButton("Вернуться назад", callback_data='back_to_start'),
                    ]
                    keyboard_markup.add(*buttons)
                    await bot.send_message(message.from_user.id, "Выберите день недели:", reply_markup=keyboard_markup)
                    waiting_for_group = False  # Сбрасываем состояние ожидания
                else:
                    await bot.send_message(message.from_user.id,
                                           "Неправильный ввод. Пожалуйста, введите корректную учебную группу.")
                    return
        else:
            # Если текст неправильный, отправьте сообщение с инструкциями или запросите ввод снова
            await bot.send_message(message.from_user.id,
                                   "Неправильный ввод. Пожалуйста, введите корректную учебную группу.")
            return
    elif waiting_for_room:
        user_input = message.text
        user_id = message.from_user.id
        waiting_for_room = await get_room_info(bot, user_id, user_input, waiting_for_room, callback_query)


@dp.callback_query_handler()
async def handle_keyboard_buttons(bot, user_id):
    await of_the_week(bot, callback_query)
    await info(bot, callback_query)
