import csv
import os
import pandas as pd


script_dir = os.path.dirname(os.path.abspath(__file__))
file_csv = os.path.join(script_dir, "../data/transactions.csv")
file_excel = os.path.join(script_dir, "../data/transactions_excel.xlsx")
