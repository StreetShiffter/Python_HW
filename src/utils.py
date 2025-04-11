import json
import os
import logging



loger_func = logging.getLogger(__name__) # логер к текущему модулю
file_handler = logging.FileHandler('../logs/example.log', encoding = 'utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
loger_func.addHandler(file_handler)
loger_func.setLevel(logging.DEBUG)

# Получаем путь к текущему скрипту
script_dir = os.path.dirname(os.path.abspath(__file__))

# Определяем путь к файлу относительно текущего скрипта
file_path = os.path.join(script_dir, "../data/operations.json")


def read_file(filename: str) -> list[dict]:
    """Функция чтения файла JSON"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Проверяем, что данные представляют собой список
        if not isinstance(data, list):
            loger_func.info("JSON файл пуст: %s", filename)
            return []

        loger_func.info("Успешное чтение JSON: %s", filename)
        return data
    except FileNotFoundError:
        print(f"Файл не найден по пути: {filename}")
        loger_func.error("Файл не найден по пути: %s", filename)
        return []
    except json.JSONDecodeError:
        print(f"Ошибка при декодировании JSON из файла: {filename}")
        loger_func.error("Ошибка при декодировании JSON из файла: %s", filename)
        return []

data = read_file(file_path)
print(data)
