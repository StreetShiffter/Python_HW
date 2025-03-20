import re


def mask_account_card(string: str) -> tuple[str, str]:
    """Функция маскировки счета/карты"""
    string_split = string.split()
    name_card_or_score = " ".join(string_split[:-1])  # Элементы имени
    number_card_or_score = string_split[-1]

    # Проверка имени карты на наличие только букв (латинских и кириллических) и пробелов
    if not re.match(r'^[A-Za-zа-яА-ЯёЁ\s]+$', name_card_or_score):
        raise ValueError("Название должно состоять из буквенных символов!")
    if not number_card_or_score.isdigit():
        raise ValueError("Номер должен состоять только из цифр!")

    return name_card_or_score, number_card_or_score


def get_date(input_string: str) -> str:
    """Функция вывода даты"""
    date_string = ""
    for item in input_string:
        clean_string = re.findall("[0-9]", item)  # Находим цифровые значения
        if clean_string:
            date_string += "".join(clean_string)
    return f"{date_string[6:8]}.{date_string[4:6]}.{date_string[0:4]}"