from typing import Union


def get_mask_card_number(number_card: Union[int, str]) -> str:
    """Функция, которая маскирует предпоследние 6 цифр"""

    card_number = str(number_card)

    return f"{card_number[:4]} {card_number[4:6]} {'**'} {'****'} {card_number[-4:]}"


def get_mask_account(number_account: Union[int, str]) -> str:
    """Функция для маскирования номера аккаунта, оставляя 4 последние цифры"""

    account_number = str(number_account)
    visible_numbers = account_number[-4:]

    return f"** {visible_numbers}"
