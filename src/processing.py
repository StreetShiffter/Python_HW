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
