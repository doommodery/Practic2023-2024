import json

from handlers.book_rooom import button_sequence


async def booking_status(callback_query, user_id):
    action = callback_query.data
    # Считываем данные из файла
    with open("booking_down.json", "r", encoding="utf-8") as file:
        json_data = file.read()

    # Преобразование строки в формат JSON
    json_dict = json.loads(json_data)

    # Шаг 1: Добавляем переменную с номером пары в конец списка с ключами
    keys_listt = button_sequence
    abc = action
    keys_listt.append(abc)

    # Шаг 2: Заменяем значение ключа '1pair' на 'booking'
    nested_dict = json_dict
    for key in keys_listt[:-1]:
        nested_dict = nested_dict[key]

    nested_dict[keys_listt[-1]] = 'booking'

    # Сохраняем обновленные данные обратно в файл
    with open("booking_down.json", "w", encoding="utf-8") as file:
        json.dump(json_dict, file, ensure_ascii=False, indent=2)

    file_path = f"C:/Users/Vadim/OneDrive/Рабочий стол/{user_id}_bookings.txt"
    with open(file_path, "a", encoding='utf-8') as file:
        booking_info = str(keys_listt) + '\n'
        file.write(booking_info)
