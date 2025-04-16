import csv
import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
file_csv = os.path.join(script_dir, "../data/transactions.csv")
file_excel = os.path.join(script_dir, "../data/transactions_excel.xlsx")


def open_csv(filename: str, delimiter=',') -> str:
    with open(filename, 'r',  encoding = 'utf-8') as file:
        reader = csv.reader(file, delimiter=delimiter)
        row = [item for item in reader]
    return row


total = open_csv(file_csv, ':')
print(total)
