import csv
import os
from typing import List, Dict, Any, Union
import pandas as pd  # type: ignore



script_dir = os.path.dirname(os.path.abspath(__file__))
file_csv = os.path.join(script_dir, "../data/transactions.csv")
file_excel = os.path.join(script_dir, "../data/transactions_excel.xlsx")


def open_csv(filename: str, delimiter: str = ';') -> List[Dict[str, Union[str, float, None]]]:
    """Функция читающая CSV файл и преобразующая данные в нужный формат."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=delimiter)

            result: List[Dict[str, Union[str, float, None]]] = []
            for row in reader:
                processed_row: Dict[str, Union[str, float, None]] = {}
                for key, value in row.items():
                    if key in ['id', 'amount']:
                        try:
                            processed_row[key] = float(value) if value else 0.0
                        except ValueError:
                            processed_row[key] = 0.0
                    else:
                        processed_row[key] = value.strip() if value else None

                result.append(processed_row)

            return result

    except Exception as error:
        raise Exception(f'Ошибка при чтении файла: {str(error)}')


def open_excel(filename: str) -> List[Dict[str, Any]]:
    """Функция читающая excel файл."""
    try:
        df = pd.read_excel(filename)
        return df.to_dict('records')
    except Exception as error:
        raise Exception(f'Ошибка при чтении файла: {str(error)}')