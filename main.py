from src.utils import read_file
from src.open_file_stat import open_csv, open_excel
from config import PATH_JSON, PATH_CSV, PATH_EXCEL
import pandas as pd



def start_choise():
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print('Выберите необходимый пункт меню:')
    print('1. Получить информацию о транзакциях из JSON-файла')
    print('2. Получить информацию о транзакциях из CSV-файла')
    print('3. Получить информацию о транзакциях из XLSX-файла')

    while True:
        user_input = str(input().strip().lower())
        if user_input == '1':
            print('Для обработки выбран JSON-файл.')
            start = read_file(PATH_JSON)
            return start
        elif user_input == '2':
            print('Для обработки выбран csv-файл.')
            start = open_csv(PATH_CSV)
            return start
        elif user_input == '3':
            print('Для обработки выбран excel-файл.')
            start = open_excel(PATH_EXCEL)
            return start
        else:
            print('Выберете операцию из списка!')
            continue

if __name__ == '__main__':
    data = start_choise()  # Запуск функции213
    print("Данные успешно загружены!")


