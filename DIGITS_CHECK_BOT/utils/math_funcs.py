import numpy as np
from tqdm import tqdm


def check_number_all_functions(number):
    result = ''
    for func in [is_simple_check, is_fibo_check]:
        result += func(number) + '\n\n'
    result += 'Ещё число &lt; 1_000_000_000_000?'
    return result


def is_simple_check(number: int) -> str:
    dividers = []
    for i in range(2, int(np.sqrt(number)) + 1):
        if number % i == 0:
            dividers.append(i)
    return f"{number} - простое, т.е. делится только на 1 и на само себя" if len(dividers) == 0 else \
        f"{number} делится на 1, {', '.join([str(x) for x in dividers])}, {number}"


def is_fibo_check(number: int, index=70) -> (int, str):
    if number == 0:
        return f"{number} - 1 член ряда Фибоначчи"
    elif number == 1:
        return f"{number} - 2 член ряда Фибоначчи"
    f_el = 0
    s_el = 1
    for i in range(3, index + 1):
        current = f_el + s_el
        f_el = s_el
        s_el = current
        if current == number:
            return f"{number} - {i} член ряда Фибоначчи"
        if current > number:
            return f"{number} не принадлежит к ряду чисел Фибоначчи"
    return f"{number} слишком большое число для проверки на принадлежность к ряду Фибоначчи"


def fibo_num(index):
    if index == 1:
        return 0
    elif index == 2:
        return 1
    else:
        return fibo_num(index - 2) + fibo_num(index - 1)


# # print(fibo_num(45))
# print(check_number_all_functions(1_000_000_000_000))
