from src.utils import read_file
from src.open_file_stat import open_csv, open_excel
from src.processing import filter_by_state, sort_by_date
from config import PATH_JSON, PATH_CSV, PATH_EXCEL
import pandas as pd


def select_file() -> list[dict]:
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print('Выберите необходимый пункт меню:')
    print('1. Получить информацию о транзакциях из JSON-файла')
    print('2. Получить информацию о транзакциях из CSV-файла')
    print('3. Получить информацию о транзакциях из XLSX-файла')

    while True:
        user_input = str(input().strip().lower())
        if user_input == '1':
            print(user_input)
            print('Для обработки выбран JSON-файл.')
            start = read_file(PATH_JSON)
            return start
        elif user_input == '2':
            print(user_input)
            print('Для обработки выбран csv-файл.')
            start = open_csv(PATH_CSV)
            return start
        elif user_input == '3':
            print(user_input)
            print('Для обработки выбран excel-файл.')
            start = open_excel(PATH_EXCEL)
            return start
        else:
            print('Выберете операцию из списка!')
            continue


def filter_status(transactions: list[dict]) -> list[dict]:
    print('Введите статус, по которому необходимо выполнить фильтрацию. '
          'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
    while True:
        user_input = input().strip().lower()
        status_executed = 'EXECUTED'
        status_canceled = 'CANCELED'
        status_pending = 'PENDING'
        if user_input == status_executed.lower():
            print(user_input)
            sorting = filter_by_state(transactions, user_input)
            print('Операции отфильтрованы по статусу "EXECUTED"')
            return sorting
        elif user_input == status_canceled.lower():
            print(user_input)
            sorting = filter_by_state(transactions, user_input)
            print('Операции отфильтрованы по статусу "CANCELED"')
            return sorting
        elif user_input == status_pending.lower():
            print(user_input)
            sorting = filter_by_state(transactions, user_input)
            print('Операции отфильтрованы по статусу "PENDING"')
            return sorting
        else:
            print(f'Статус операции {user_input} недоступен.')
            continue


if __name__ == '__main__':
    data = select_file()  # Запуск функции
    filtered_data = filter_status(data)
    print("Данные успешно загружены!")
