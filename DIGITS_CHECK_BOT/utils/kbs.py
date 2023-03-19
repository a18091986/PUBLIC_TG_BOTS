from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_items = ['!Что_умеет_бот', "!Ограничения_на_числа",
                   '!Какие_проверки_реализованы', '!Какие_проверки_планируются']


def get_main_menu_kb() -> ReplyKeyboardMarkup:
    return get_kb(main_menu_items, 0)


def get_kb(menu_items: list, split_insert_add_index=len(main_menu_items)) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([], resize_keyboard=True)
    for item in menu_items[:split_insert_add_index]:
        kb.insert(KeyboardButton(item))
    for item in menu_items[split_insert_add_index:]:
        kb.add(KeyboardButton(item))
    return kb
