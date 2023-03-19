import configparser
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from utils.create_bot import bot
from utils.kbs import get_main_menu_kb
from utils.logging_utils import log_in_file_and_print_in_terminal

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
MAX_NUMBER = int(config['CONSTANTS']['MAX_NUMBER'])


async def start_command(msg: types.Message):
    answer = 'выбери пункт меню или отправь мне какое-нибудь число &lt; 1_000_000_000_000'
    await bot.send_message(chat_id=msg.from_user.id, text=answer, parse_mode='html', reply_markup=get_main_menu_kb())
    log_in_file_and_print_in_terminal(msg=f"SEND TO USER {msg.from_user.id} - {msg.from_user.username}\n"
                                          f"{answer}\n on message \n{msg.text}\n\n",
                                      print_in_terminal=False, loglevel=3)


async def about(msg: types.Message):
    answer = ''
    await bot.send_message(chat_id=msg.from_user.id, text=answer, parse_mode='html', reply_markup=get_main_menu_kb())
    log_in_file_and_print_in_terminal(msg=f"SEND TO USER {msg.from_user.id} - {msg.from_user.username}\n"
                                          f"{answer}\n on message \n{msg.text}\n\n",
                                      print_in_terminal=False, loglevel=3)


async def constraints(msg: types.Message):
    answer = f"Числа должны быть:\n- целые\n- положительные\n- меньше {MAX_NUMBER}\n"
    await bot.send_message(chat_id=msg.from_user.id, text=answer, parse_mode='html', reply_markup=get_main_menu_kb())
    log_in_file_and_print_in_terminal(msg=f"SEND TO USER {msg.from_user.id} - {msg.from_user.username}\n"
                                          f"{answer}\n on message \n{msg.text}\n\n",
                                      print_in_terminal=False, loglevel=3)


async def verification_done(msg: types.Message):
    await bot.send_message(chat_id=msg.from_user.id, text='в разработке',
                           reply_markup=get_main_menu_kb())


async def verification_plan(msg: types.Message):
    await bot.send_message(chat_id=msg.from_user.id, text='в разработке',
                           reply_markup=get_main_menu_kb())


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(start_command, Command(commands=['В_главное_меню'], prefixes=['!']))
    dp.register_message_handler(about, Command(commands=['Что_умеет_бот'], prefixes=['!']))
    dp.register_message_handler(constraints, Command(commands=['Ограничения_на_числа'], prefixes=['!']))
    dp.register_message_handler(verification_done, Command(commands=['Какие_проверки_реализованы'], prefixes=['!']))
    dp.register_message_handler(verification_plan, Command(commands=['Какие_проверки_планируются'], prefixes=['!']))
