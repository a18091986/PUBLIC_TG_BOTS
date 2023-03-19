import configparser

from utils.create_bot import dp, bot
from aiogram import executor
from handlers import information, calculation
from utils.kbs import get_main_menu_kb
from utils.logging_utils import *

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
bot_users = config['BOT_START_SEND_USERS']['BOT_USERS']
MAX_NUMBER = int(config['CONSTANTS']['MAX_NUMBER'])


information.register_handlers(dp)
calculation.register_handlers(dp)


async def on_startup(_):
    for user in bot_users:
        try:
            await bot.send_message(user, f'Бот запущен', reply_markup=get_main_menu_kb(), parse_mode='html')
            log_in_file_and_print_in_terminal(msg=f"SEND TO USER {user} start_message",
                                                  print_in_terminal=False, loglevel=3)
        except Exception as e:
            log_in_file_and_print_in_terminal(msg=f"Can't send user {user}: {e}", print_in_terminal=False, loglevel=3)


if __name__ == '__main__':
    print("Бот онлайн")
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)