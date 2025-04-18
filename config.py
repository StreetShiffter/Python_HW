import os
import json

script_dir = os.path.dirname(os.path.abspath(__file__))

# Определяем путь к файлу относительно текущего скрипта
PATH_JSON = os.path.join(script_dir, "./data/operations.json")
PATH_CSV = os.path.join(script_dir, "../data/transactions.csv")
PATH_EXEL = os.path.join(script_dir, "../data/transactions_exel.xlsx")

