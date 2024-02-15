import json


async def deleting_a_reservation(user_id):
    # Формируем путь к текстовому файлу
    file_path = f"C:/Users/Vadim/OneDrive/Рабочий стол/{user_id}_bookings.txt"

    try:
        # Открываем файл на чтение и считываем первую строку
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readline()

        # Преобразуем строку в список
        booking_list = eval(content)

        # Удаляем первую строку из файла
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines[1:])

        # Открываем JSON-файл на чтение
        json_file_path = "booking_down.json"
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            # Загружаем JSON-словарь
            booking_dict = json.load(json_file)

            # Ищем соответствующие ключи в словаре и обновляем значения
            current_dict = booking_dict
            for key in booking_list[:-1]:
                current_dict = current_dict[key]

            last_key = booking_list[-1]
            if last_key in current_dict and current_dict[last_key] == "booking":
                current_dict[last_key] = "unbooking"

        # Записываем обновленный словарь обратно в JSON-файл
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(booking_dict, json_file, ensure_ascii=False, indent=2)

        # Возвращаем полученный список

        return "Бронирование отменено!"

    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        print(f"Файл {file_path} или {json_file_path} не найден.")
        return None
    except Exception as e:
        # Обработка других исключений
        print(f"Произошла ошибка: {e}")
        return None