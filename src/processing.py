def filter_by_state(list_data: list[dict[str,str]], state: str = 'EXECUTED') -> list[dict[str, str | int]]:
    """Функция сортировки словарей по значению"""
    list_dict_check = []
    for item in list_data:
        if item.get("state") == state:
            list_dict_check.append(item)

    return list_dict_check


# test = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
# result = filter_by_state(test)
# print(result)


def sort_by_date(list_check_date: list[dict], value_sort:bool = True) -> list[dict]:
    """Функция сортировки даты"""
    sorting = sorted(list_check_date, key=lambda x: x["date"], reverse = not value_sort)
    return sorting


test_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
result_data = sort_by_date(test_data)
print(result_data)
