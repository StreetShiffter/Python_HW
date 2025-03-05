import re

from masks import get_mask_card_number


def mask_account_card(string: str) -> tuple[str, str]:
    """Функция маскировки счета/карты"""
    string_split = string.split()
    name_card_or_score = " ".join(string_split[:-1])  # Элементы имени
    number_card_or_score = string_split[-1]  # Элемент номера

    return name_card_or_score, number_card_or_score


test = "Visa Platinum 8990922113665229"  # Для предварительного тестирования
name_card, number_card = mask_account_card(test)

masked_number = get_mask_card_number(number_card)
print(f"{name_card}: {masked_number}")


def get_date(input_string: str) -> str:
    """Функция вывода даты"""
    date_string = ""
    for item in input_string:
        clean_string = re.findall("[0-9]", item)  # Находим цифровые значения
        if clean_string:
            date_string += "".join(clean_string)
    return f"{date_string[6:8]}.{date_string[4:6]}.{date_string[0:4]}"


test = "2024-03-11T02:26:18.671407"
print(get_date(test))
