from typing import Generator


# def filter_by_currency(transactions: list[dict], code: str )-> Generator[dict]:
#     '''Функция предоставления доступных транзакций'''
#     if not transactions:
#         raise ValueError("Передано пустое значение!")
#     for item in transactions:
#         if item["operationAmount"]["currency"]["code"] == code:
#             yield item
#
#
# def transaction_descriptions(transactions: list[dict]) -> Generator[str]:
#     '''Функция-генератор для выдачи описания транзакции'''
#     if not transactions:
#         raise ValueError("Передано пустое значение!")
#
#     for item in transactions:
#         if "description" not in item:
#             yield 'Отсутствует описание'
#         else:
#             yield item["description"]

def card_number_generator(start: int, end: int)-> Generator[str]:
    '''Функция-генератор номеров карты'''
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Введите целые числа!")
    if start < 0 or end < 0:
        raise ValueError("Неверное значение")
    if start > end :
        raise ValueError("Стартовое значение превышает конечное!")

    for number in range(start, end+1):
        # Преобразуем число в строку
        card_number = f"{number:016}"

        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number.strip() # Убираем лишние пробелы
