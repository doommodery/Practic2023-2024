from aiogram import types
import json

from aiogram.types import CallbackQuery

from handlers.book_rooom import button_sequence


def find_and_flatten_unbooking_pairs(callback_query: CallbackQuery, json_file_path):
    button_sequence.append(callback_query.data)
    keys = button_sequence
    print(keys)

    def find_unbooking_pairs(data, keys):
        result = []
        current_level = data

        for key in keys:
            if key in current_level:
                result.append(current_level[key])
                current_level = current_level[key]

        return result

    with open(json_file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    unbooking_values = find_unbooking_pairs(json_data, keys)

    def flatten(d):
        result = []

        def traverse(obj):
            for k, v in obj.items():
                if isinstance(v, dict):
                    traverse(v)
                elif k.endswith('pair') and v == 'unbooking':
                    result.append(k)

        traverse(d)
        return result

    flattened_values = flatten(unbooking_values[-1])
    return flattened_values

