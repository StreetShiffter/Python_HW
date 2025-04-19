from typing import Union
import logging
import os

# Получаем путь к текущему скрипту
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(script_dir, "../logs/example.log")

loger_func = logging.getLogger(__name__) # логер к текущему модулю
file_handler = logging.FileHandler(file_path_1, encoding = 'utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
loger_func.addHandler(file_handler)
loger_func.setLevel(logging.DEBUG)




def get_mask_card_number(number_card: Union[int, str]) -> str:
    """Функция, которая маскирует предпоследние 6 цифр"""
    card_number = str(number_card).replace(" ", "")
    try:
        if not card_number.isdigit():  # Проверка на числовое значение
            raise ValueError("Введите числовое значение")

        if len(card_number) == 16:  # Маскировка для 16 символов
            masked_number =  f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
            loger_func.info("Успешная маскировка номера карты: %s", masked_number)
            return masked_number

        elif len(card_number) == 21:  # Маскировка для 21 символа
            masked_number = f"{card_number[:11]}******{card_number[-4:]}"
            loger_func.info("Успешная маскировка номера карты: %s", masked_number)
            return masked_number

        raise ValueError("Неверный номер карты! Введите 16 или 21 символ.")
    except ValueError as e:
        loger_func.error("%s", str(e), exc_info=True)
        raise




def get_mask_account(number_account: Union[int, str]) -> str:
    """Функция для маскирования номера аккаунта, оставляя 4 последние цифры"""
    account_number = str(number_account).replace(" ", "")
    visible_numbers = account_number[-4:]
    try:
        if not visible_numbers.isdigit():  # Проверка на числовое значение
            raise ValueError("Введите числовое значение")
        if len(visible_numbers) < 4:  # Проверка на длину
            raise ValueError("Короткий номер")
    except ValueError as t:
        loger_func.error("%s", number_account, exc_info=True)
        raise


    masked_account_number = f"** {visible_numbers}"
    loger_func.info("Успешная маскировка номера карты: %s", number_account)
    return masked_account_number

# test0 = "1230 8520 9632 7412"
# get_mask_card_number(test0)
# test = "sfvf"
# get_mask_account(test)

