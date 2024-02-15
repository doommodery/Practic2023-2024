import json

from handlers.book_rooom import button_sequence


def booking_statuss():
    # Считываем данные из файла
    with open("booking_down.json", "r", encoding="utf-8") as file:
        json_data = file.read()

    # Преобразование строки в формат JSON
    json_dict = json.loads(json_data)

    # Шаг 1: Добавляем переменную с номером пары в конец списка с ключами
    keys_list = button_sequence
    abc = '1pair'
    keys_list.append(abc)

    # Шаг 2: Заменяем значение ключа '1pair' на 'booking'
    nested_dict = json_dict
    for key in keys_list[:-1]:
        nested_dict = nested_dict[key]
    print(nested_dict())
    nested_dict[keys_list[-1]] = 'booking'

    # Сохраняем обновленные данные обратно в файл
    with open("booking_down.json", "w", encoding="utf-8") as file:
        json.dump(json_dict, file, ensure_ascii=False, indent=2)



