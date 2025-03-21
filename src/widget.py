import re


def mask_account_card(string: str) -> tuple[str, str]:
    """Функция маскировки счета/карты"""
    string_split = string.split()
    name_card_or_score = " ".join(string_split[:-1])  # Элементы имени
    number_card_or_score = string_split[-1]

    # Проверка имени карты на наличие только букв (латинских и кириллических) и пробелов
    if not re.match(r"^[A-Za-zа-яА-ЯёЁ\s]+$", name_card_or_score):
        raise ValueError("Название должно состоять из буквенных символов!")
    if not number_card_or_score.isdigit():
        raise ValueError("Номер должен состоять только из цифр!")

    return name_card_or_score, number_card_or_score


def get_date(input_string: str) -> str:
    """Функция вывода даты в формате DD.MM.YYYY"""
    if input_string is None or input_string == "":
        raise TypeError("Входные данные пустые или имеют неверные символы")

    if len(input_string) < 19 or len(input_string) > 26:
        raise ValueError("Неверный формат данных: длина должна быть от 19 до 26 символов")

    clean_string = re.findall("[0-9]", input_string)
    date_string = "".join(clean_string)
    correct_date = f"{date_string[6:8]}.{date_string[4:6]}.{date_string[0:4]}"
    if len(correct_date) < 8 or len(correct_date) > 10:
        raise ValueError("Неверный формат данных: Type error ISO 8601")
    return correct_date


# test = "2024-03-11T02:26:18.67140"
# rt = get_date(test)
# print(rt)
