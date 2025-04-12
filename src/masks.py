from typing import Union
import logging

loger_func = logging.getLogger(__name__) # логер к текущему модулю
file_handler = logging.FileHandler('../logs/example.log', encoding = 'utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
loger_func.addHandler(file_handler)
loger_func.setLevel(logging.DEBUG)




def get_mask_card_number(number_card: Union[int, str]) -> str:
    """Функция, которая маскирует предпоследние 6 цифр"""
    card_number = str(number_card).replace(" ", "")
    if not card_number.isdigit():  # Проверка на числовое значение
        loger_func.error("Введено нечисловое значение: %s", number_card)
        raise ValueError("Введите числовое значение")

    if len(card_number) == 16:  # Маскировка для 16 символов
        masked_number =  f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        loger_func.info("Успешная маскировка номера карты: %s", masked_number)
        return masked_number

    elif len(card_number) == 21:  # Маскировка для 21 символа
        masked_number = f"{card_number[:11]}******{card_number[-4:]}"
        loger_func.info("Успешная маскировка номера карты: %s", masked_number)
        return masked_number

    loger_func.error("Неверный номер карты! Введено: %s", number_card)
    raise ValueError("Неверный номер карты! Введите 16 или 21 символ.")

test = 5
get_mask_card_number(test)


def get_mask_account(number_account: Union[int, str]) -> str:
    """Функция для маскирования номера аккаунта, оставляя 4 последние цифры"""
    account_number = str(number_account)
    visible_numbers = account_number[-4:]
    if not visible_numbers.isdigit():  # Проверка на числовое значение
        loger_func.error("Введено нечисловое значение: %s", number_account)
        raise ValueError("Введите числовое значение")
    if len(visible_numbers) < 4:  # Проверка на длину
        loger_func.error("Не корректная длина номера: %s", number_account)
        raise ValueError("Короткий номер")

    masked_account_number = f"** {visible_numbers}"
    loger_func.info("Успешная маскировка номера карты: %s", number_account)
    return masked_account_number


test = "o"
get_mask_card_number(test)

