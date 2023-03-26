import configparser
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command

from utils.common import add_user_in_txt
from utils.create_bot import bot
from utils.kbs import get_main_menu_kb
from utils.logging_utils import log_in_file_and_print_in_terminal

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
MAX_NUMBER = int(config['CONSTANTS']['MAX_NUMBER'])


async def start_command(msg: types.Message):
    add_user_in_txt(msg.from_user.id)
    answer = f'выбери пункт меню или отправь мне какое-нибудь число &lt; {MAX_NUMBER}'
    await bot.send_message(chat_id=msg.from_user.id, text=answer, parse_mode='html', reply_markup=get_main_menu_kb())
    log_in_file_and_print_in_terminal(msg=f"SEND TO USER {msg.from_user.id} - {msg.from_user.username}\n"
                                          f"{answer}\n on message \n{msg.text}\n\n",
                                      print_in_terminal=False, loglevel=3)


async def about(msg: types.Message):
    add_user_in_txt(msg.from_user.id)
    answer = f'Данный бот собирается выяснять различные интересные факты о присылаемых ему числах.\n' \
             f'Под капотом:\npython (aiogram)\nС, C#, C++ (функционал)'
    await bot.send_message(chat_id=msg.from_user.id, text=answer, parse_mode='html', reply_markup=get_main_menu_kb())
    log_in_file_and_print_in_terminal(msg=f"SEND TO USER {msg.from_user.id} - {msg.from_user.username}\n"
                                          f"{answer}\n on message \n{msg.text}\n\n",
                                      print_in_terminal=False, loglevel=3)


async def constraints(msg: types.Message):
    add_user_in_txt(msg.from_user.id)
    answer = f"Числа должны быть:\n- целые\n- положительные\n- меньше {MAX_NUMBER}\n"
    await bot.send_message(chat_id=msg.from_user.id, text=answer, parse_mode='html', reply_markup=get_main_menu_kb())
    log_in_file_and_print_in_terminal(msg=f"SEND TO USER {msg.from_user.id} - {msg.from_user.username}\n"
                                          f"{answer}\n on message \n{msg.text}\n\n",
                                      print_in_terminal=False, loglevel=3)


async def verification_done(msg: types.Message):
    add_user_in_txt(msg.from_user.id)
    answer = f'Реализовано: \n' \
             f'1. Поиск всех делителей числа (проверка на простоту)\n' \
             f'2. Проверка на принадлженость числа к ряду чисел Фибоначчи\n'
    await bot.send_message(chat_id=msg.from_user.id, text=answer, parse_mode='html', reply_markup=get_main_menu_kb())
    log_in_file_and_print_in_terminal(msg=f"SEND TO USER {msg.from_user.id} - {msg.from_user.username}\n"
                                          f"{answer}\n on message \n{msg.text}\n\n",
                                      print_in_terminal=False, loglevel=3)


async def verification_plan(msg: types.Message):
    add_user_in_txt(msg.from_user.id)
    answer = f'В планах: \n' \
             f'1. Проверка числа на "совершенство"\n' \
             f'2. Проверка на принадлежность числа к ряду чисел Мерсенна\n' \
             f'3. Поиск дружественных чисел\n' \
             f'4. Проверка числа на принадлежность к множеству чисел Смита\n' \
             f'5. Проверка числа на принадлежность к числам Софи Жермеен\n' \
             f'6. Проверка числа на принадлежность к числам Люка\n' \
             f'7. Проверка числа на принадлежность к числам Ферма\n' \
             f'8. Проверка числа на принадлежность к числам Бернулли\n' \
             f'9. Поиск факториала числа\n' \
             f'10. Etc... \n' \

    await bot.send_message(chat_id=msg.from_user.id, text=answer, parse_mode='html', reply_markup=get_main_menu_kb())
    log_in_file_and_print_in_terminal(msg=f"SEND TO USER {msg.from_user.id} - {msg.from_user.username}\n"
                                          f"{answer}\n on message \n{msg.text}\n\n",
                                      print_in_terminal=False, loglevel=3)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(start_command, Command(commands=['В_главное_меню'], prefixes=['!']))
    dp.register_message_handler(about, Command(commands=['О_боте'], prefixes=['!']))
    dp.register_message_handler(constraints, Command(commands=['Ограничения_на_числа'], prefixes=['!']))
    dp.register_message_handler(verification_done, Command(commands=['Какие_проверки_реализованы'], prefixes=['!']))
    dp.register_message_handler(verification_plan, Command(commands=['Какие_проверки_планируются'], prefixes=['!']))
