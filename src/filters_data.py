import re


def finder_info(data_list: list[dict], input_string: str) -> list[dict]:
    '''Функция, фильтрующая операции по описанию'''
    pattern = re.compile(input_string, re.IGNORECASE)
    filter_data = []
    for item in data_list:
        if any(pattern.search(str(x)) for x in item.keys() | item.values()):
            filter_data.append(item)  # Добавляем словарь в результаты

    return filter_data

