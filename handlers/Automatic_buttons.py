
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from googletrans import Translator


def translate_and_create_buttons(values):
    перевод = {
        '1pair': '1 пара',
        '2pair': '2 пара',
        '3pair': '3 пара',
        '4pair': '4 пара',
        '5pair': '5 пара',
        '6pair': '6 пара',
        '7pair': '7 пара'
    }
    translated_values = [перевод.get(пара, пара) for пара in values]

    # Создаем инлайновские кнопки
    inline_keyboard = InlineKeyboardMarkup(row_width=1)
    for original, translation in zip(values, translated_values):
        button = InlineKeyboardButton(text=translation, callback_data=f'{original}')
        inline_keyboard.add(button)

    back_button = InlineKeyboardButton(text='Вернуться назад', callback_data='back_to_start')
    inline_keyboard.add(back_button)

    return inline_keyboard


async def send_buttons(chat_id, bot, result_list):
    values = result_list
    print(result_list)
    translated_keyboard = translate_and_create_buttons(values)
    print(translated_keyboard)
    await bot.send_message(chat_id, 'Выберите академический час:', reply_markup=translated_keyboard)






