import csv
import os
from typing import List, Any
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
file_csv = os.path.join(script_dir, "../data/transactions.csv")
file_excel = os.path.join(script_dir, "../data/transactions_excel.xlsx")


def open_csv(filename: str, delimiter: str = ',') -> List[dict[str, Any]]:
    """Функция читающая CSV файл."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=delimiter)
            return list(reader)
    except Exception as error:
        raise Exception(f'Ошибка при чтении файла: {str(error)}')


def open_excel(filename: str) -> List[dict[Any, Any]]:
    """Функция читающая excel файл."""
    try:
        df = pd.read_excel(filename)
        return df.to_dict('records')
    except Exception as error:
        raise Exception(f'Ошибка при чтении файла: {str(error)}')