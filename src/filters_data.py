import re
from collections import Counter


def finder_info(data_list: list[dict], input_string: str) -> list[dict]:
    """Функция, фильтрующая операции по описанию."""
    pattern = re.compile(input_string, re.IGNORECASE)
    filter_data = []

    for item in data_list:
        # Проверяем как ключи, так и значения
        if any(pattern.search(str(key)) for key in item.keys()) or \
         any(pattern.search(str(value)) for value in item.values()):
            filter_data.append(item) # Добавляем словарь в результаты

    return filter_data


def counter_description(transaction_list: list[dict], list_description: list) -> dict:
    """Функция подсчета количества операций"""
    count: dict = dict(Counter())
    for descr_pat in list_description:
        count[descr_pat] = 0
        for transaction in transaction_list:
            description = transaction.get("description", "").lower()
            if description == descr_pat.lower():
                count[descr_pat] += 1

    return count
# listing = ["Перевод организации","Открытие вклада","Перевод со счета на счет","Перевод с карты на счет"]
# data = [{
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Открытие вклада",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   },{
#     "id": 587085106,
#     "state": "PENDING",
#     "date": "2018-03-23T10:45:06.972075",
#     "operationAmount": {
#       "amount": "48223.05",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Открытие вклада",
#     "to": "Счет 41421565395219882431"
#   },{
#     "id": 142264268,
#     "state": "CANCELED",
#     "date": "2019-04-04T23:20:05.206878",
#     "operationAmount": {
#       "amount": "79114.93",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод со счета на счет",
#     "from": "Счет 19708645243227258542",
#     "to": "Счет 75651667383060284188"
#   },{
#     "id": 580054042,
#     "state": "EXECUTED",
#     "date": "2018-06-20T03:59:34.851630",
#     "operationAmount": {
#       "amount": "96350.51",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод с карты на счет",
#     "from": "МИР 3766446452238784",
#     "to": "Счет 86655182730188443980"
#   }
# ]
#
# result = counter_description(data,listing)
# print(result)
