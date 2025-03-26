from typing import Generator


def filter_by_currency(transactions: list[dict], code: str )-> Generator[dict]:
    '''Функция предоставления доступных транзакций'''
    if not transactions :
        raise ValueError("Передано пустое значение!")
    for item in transactions:
        if item["operationAmount"]["currency"]["code"] == code:
            yield item


# def transaction_descriptions(start: int, end: int)-> Generator:
#     pass
#
# def card_number_generator():
#     pass