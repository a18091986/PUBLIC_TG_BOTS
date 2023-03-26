import configparser
from aiogram import types, Dispatcher

from utils.common import add_user_in_txt
from utils.create_bot import bot
from utils.kbs import get_kb
from utils.logging_utils import log_in_file_and_print_in_terminal
from utils.math_fucs import calculate_factorial, calculate_triangle_number
from utils.math_funcs import check_number_all_functions
import subprocess
from pathlib import Path

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
MAX_NUMBER = int(config['CONSTANTS']['MAX_NUMBER'])
FACTORIAL_CONSTRAINT = int(config['CONSTANTS']['FACTORIAL'])
TRIANGLE_CONSTRAINT = int(config['CONSTANTS']['TRIANGLE'])


async def calculate(msg: types.Message):
    add_user_in_txt(msg.from_user.id)
    number = int(msg.text)
    decimal_1 = number.split('.')
    decimal_2 = number.split(',')
    describe_number_str = f"Тут тебе не chatGPT!\n" \
                          f"Введи число, которое:\n- целое\n- положительное\n- меньше {MAX_NUMBER}\n"
    if number.isdigit():
        if str(int(number)) == number:
            if int(number) > MAX_NUMBER or int(number) <= 0:
                await bot.send_message(chat_id=msg.from_user.id, text=describe_number_str,
                                       reply_markup=get_kb(['!В_главное_меню']))
                log_in_file_and_print_in_terminal(msg=f"SEND TO USER {msg.from_user.id} - {msg.from_user.username}\n"
                                                      f"{describe_number_str}\n on message \n{msg.text}\n\n",
                                                  print_in_terminal=False, loglevel=3)
            else:
                path = str(Path('c_funcs', 'c_func.exe'))
                # print(path)
                subprocess.run([path, number], capture_output=True, text=True)
                with open('answer.txt', 'r', encoding='utf-8') as f:
                    answer = f.read()
                if number < FACTORIAL_CONSTRAINT:
                    answer += f"Факториал числа {number} (рассчитывается для чисел < {FACTORIAL_CONSTRAINT})" \
                              f"{calculate_factorial(number)}\n"
                if number < TRIANGLE_CONSTRAINT:
                    answer += f"треугольное число для {number} (рассчитывается для чисел < {TRIANGLE_CONSTRAINT})" \
                              f"{calculate_triangle_number(number)}\n"
                await bot.send_message(chat_id=msg.from_user.id, text=answer,
                                       reply_markup=get_kb(['!В_главное_меню']), parse_mode='html')
                log_in_file_and_print_in_terminal(msg=f"SEND TO USER {msg.from_user.id} - {msg.from_user.username}\n"
                                                      f"{answer}\n on message \n{msg.text}\n\n",
                                                  print_in_terminal=False, loglevel=3)
                # await bot.send_message(chat_id=msg.from_user.id, text=check_number_all_functions(int(number)),
                #                        reply_markup=get_kb(['!В_главное_меню']), parse_mode='html')
        else:
            await bot.send_message(chat_id=msg.from_user.id, text=describe_number_str,
                                   reply_markup=get_kb(['!В_главное_меню']))
            log_in_file_and_print_in_terminal(msg=f"SEND TO USER {msg.from_user.id} - {msg.from_user.username}\n"
                                                  f"{describe_number_str}\n on message \n{msg.text}\n\n",
                                              print_in_terminal=False, loglevel=3)
    elif (len(decimal_1) == 2 and decimal_1[0].isdigit() and decimal_1[1].isdigit()) or \
            (len(decimal_2) == 2 and decimal_2[0].isdigit() and decimal_2[1].isdigit()):
        await bot.send_message(chat_id=msg.from_user.id, text=describe_number_str,
                               reply_markup=get_kb(['!В_главное_меню']))
        log_in_file_and_print_in_terminal(msg=f"SEND TO USER {msg.from_user.id} - {msg.from_user.username}\n"
                                              f"{describe_number_str}\n on message \n{msg.text}\n\n",
                                          print_in_terminal=False, loglevel=3)
    else:
        await bot.send_message(chat_id=msg.from_user.id, text=describe_number_str,
                               reply_markup=get_kb(['!В_главное_меню']))
        log_in_file_and_print_in_terminal(msg=f"SEND TO USER {msg.from_user.id} - {msg.from_user.username}\n"
                                              f"{describe_number_str}\n on message \n{msg.text}\n\n",
                                          print_in_terminal=False, loglevel=3)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(calculate)
