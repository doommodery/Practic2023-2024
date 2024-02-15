# main.py
from aiogram import executor
import logging
#import groops
from bot import dp, bot
from handlers import start, callbacks, help, utils, schedule, info_auditorium
import handlers
logging.basicConfig(level=logging.INFO)
selected_options = {}

if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)