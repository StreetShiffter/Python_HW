from masks import get_mask_card_number


def mask_account_card(string: str) -> tuple[str, str]:
    """Функция маскировки счета/карты"""
    string_split = string.split()  # Разделяем строку на элементы
    name_card_or_score = " ".join(string_split[:-1])  # Элементы имени
    number_card_or_score = string_split[-1]  # Элемент номера

    return name_card_or_score, number_card_or_score


test = "Visa Platinum 8990922113665229"
name_card, number_card = mask_account_card(test)

masked_number = get_mask_card_number(number_card)
print(f"{name_card}: {masked_number}")
