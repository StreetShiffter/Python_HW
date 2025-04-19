import re
from collections import Counter


def finder_info(data_list: list[dict], input_string: str) -> list[dict]:
    """Функция, фильтрующая операции по описанию"""
    pattern = re.compile(input_string, re.IGNORECASE)
    filter_data = []
    for item in data_list:
        if any(pattern.search(str(x)) for x in item.keys() | item.values()):
            filter_data.append(item)  # Добавляем словарь в результаты

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
