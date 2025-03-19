from typing import Union
import pytest


def get_mask_card_number(number_card: Union[int, str]) -> str:
    """Функция, которая маскирует предпоследние 6 цифр"""
    card_number = str(number_card).replace(" ", "")
    if len(card_number) < 16 or len(card_number) > 16: # Проверка на длину
        raise ValueError("Введите ровно 16 символов карты!")
    if not card_number.isdigit(): #Проверка на числовое значение
        raise ValueError("Введите числовое значение")


    return f"{card_number[:4]} {card_number[4:6]}{'**'} {'****'} {card_number[-4:]}"


def get_mask_account(number_account: Union[int, str]) -> str:
    """Функция для маскирования номера аккаунта, оставляя 4 последние цифры"""
    account_number = str(number_account)
    visible_numbers = account_number[-4:]
    if not visible_numbers.isdigit(): #Проверка на числовое значение
        raise ValueError("Введите числовое значение")
    if len(visible_numbers) < 4: # Проверка на длину
        raise ValueError("Короткий номер")


    return f"** {visible_numbers}"

test = "1234 5678 9876 5435"
result = get_mask_account(test)
print(result)


