from src.utils import read_file
import os

# Получаем путь к текущему скрипту
script_dir = os.path.dirname(os.path.abspath(__file__))

# Определяем путь к файлу относительно текущего скрипта
file_path = os.path.join(script_dir, "data","operations.json")

if __name__ == '__main__':
    data = read_file(file_path)
    print(data)