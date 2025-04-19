from datetime import datetime
import re

def filter_by_state(list_data: list[dict[str, str]], state: str = "EXECUTED") -> list[dict]:
    """Функция сортировки словарей по значению"""
    list_dict_check = []
    for item in list_data:
        if item.get("state") == state:
            list_dict_check.append(item)

    return list_dict_check


def sort_by_date(list_check_date: list[dict], value_sort: bool = True) -> list[dict]:
    """Функция сортировки даты"""
    for item in list_check_date:
        if "date" not in item or item["date"] is None or item["date"].strip() == "":
            raise TypeError("Отсутствует дата в одном из элементов")
        if isinstance(item["date"], str) and item["date"].isalpha():
            raise TypeError("Значение даты должно быть числовым значением")
    sorting = sorted(list_check_date, key=lambda x: x["date"], reverse=value_sort)
    return sorting



# def sort_by_date_proper(transactions: list[dict], reverse: bool = False) -> list[dict]:
#     """Сортирует список транзакций по дате для нестандартного формата данных."""
#
#     def extract_date(transaction: dict):
#         try:
#             # Извлекаем строку с данными
#             data_str = next(iter(transaction.values()))
#             # Разбиваем по точкам с запятой и берем 3-й элемент (индекс 2) - дату
#             date_str = data_str.split(';')[2]
#             # Преобразуем дату в datetime объект
#             return datetime.fromisoformat(date_str.replace('Z', '+00:00'))
#         except (ValueError, IndexError, AttributeError):
#             return datetime.min
#
#     return sorted(transactions, key=extract_date, reverse=reverse)
