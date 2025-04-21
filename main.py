from config import PATH_CSV, PATH_EXCEL, PATH_JSON
from src.filters_data import finder_info
from src.masks import get_mask_account
from src.open_file_stat import open_csv, open_excel
from src.processing import sort_by_date
from src.utils import read_file
from src.widget import get_date
from typing import List, Dict, Any, Union



def select_file() -> list[dict]:
    """Функция выбора файла с транзакциями"""
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )

    while True:
        user_input = str(input().strip().lower())
        if user_input == "1":
            print(user_input)
            print("Для обработки выбран JSON-файл.")
            start = read_file(PATH_JSON)
            return start
        elif user_input == "2":
            print(user_input)
            print("Для обработки выбран csv-файл.")
            start = open_csv(PATH_CSV)
            return start
        elif user_input == "3":
            print(user_input)
            print("Для обработки выбран excel-файл.")
            start = open_excel(PATH_EXCEL)
            return start
        else:
            print("Выберете операцию из списка!")
            continue


def filter_status(transactions: list[dict]) -> list[dict]:
    """Функция запроса статуса операции"""
    print(
        "Введите статус, по которому необходимо выполнить фильтрацию. "
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )
    while True:
        user_input = input().strip().lower()
        status_executed = ["EXECUTED", "CANCELED", "PENDING"]
        if user_input.upper() in status_executed:
            print(user_input)
            sorting = finder_info(transactions, user_input)
            print(f"Операции отфильтрованы по статусу {user_input.upper()}")
            return sorting
        else:
            print(f"Статус операции {user_input} недоступен.")
            continue


def sorting_question(transaction_filter: list[dict]) -> list[dict]:
    """Функция сортировки по критериям"""
    print("Отсортировать операции по дате? (Да/Нет)")
    result = list(transaction_filter)  # Инициализируем result заранее

    while True:  # Первый вопрос: нужна ли сортировка
        sort_decision = input().strip().lower()
        if sort_decision == "нет":
            break
        elif sort_decision == "да":

            while True:  # Второй вопрос: тип сортировки
                print("Отсортировать по возрастанию или по убыванию?")
                sort_type = input().strip().lower()
                if sort_type == "по возрастанию":
                    result = list(sort_by_date(result))
                    break
                elif sort_type == "по убыванию":
                    result = list(sort_by_date(result, False))
                    break
                else:
                    print('Ошибка: введите "по возрастанию" или "по убыванию"')
            break
        else:
            print('Ошибка: введите "Да" или "Нет"')

    while True:  # Третий вопрос: сортировка по валюте
        print("Выводить только RUB транзакции? Да/Нет")
        answer = input().strip().lower()
        if answer == "да":
            result = [
                t
                for t in result
                if any(str(v).strip().upper() == "RUB" for v in t.values() if isinstance(v, (str, int, float)))
            ]
            break
        elif answer == "нет":
            break
        else:
            print('Ошибка: введите "Да" или "Нет"')

    while True:  # Четвертый вопрос: фильтр по ключевому слову
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_insert = input().strip().lower()
        if user_insert == "да":
            user_word = input("Введите слово: ").strip().lower()
            result = list(finder_info(result, user_word))
            break
        elif user_insert == "нет":
            break
        else:
            print('Ошибка: введите "Да" или "Нет"')

    return result


def get_mask_card_number(card_info: str) -> str:
    """Функция, которая маскирует номер карты в формате 'Visa Platinum 1234 56** **** 9012'"""
    if not card_info or not isinstance(card_info, str):
        return "N/A"

    # Разделяем название карты и номер
    parts = card_info.split()
    card_name = " ".join(parts[:-1]) if len(parts) > 1 else ""
    card_number = parts[-1] if parts else ""

    # Проверяем, что номер карты состоит из цифр
    if not card_number.isdigit():
        return card_info  # Возвращаем исходную строку, если не можем распознать номер

    # Маскируем номер карты
    if len(card_number) == 16:
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    elif len(card_number) == 21:
        masked_number = f"{card_number[:11]}******{card_number[-4:]}"
    else:
        return card_info  # Возвращаем исходную строку, если номер нестандартный

    # Собираем результат
    if card_name:
        return f"{card_name} {masked_number}"
    return masked_number


def print_transactions(transactions: List[Dict[str, Any]]) -> None:
    """Печатает транзакции в заданном формате"""
    print("\nПрограмма: Распечатываю итоговый список транзакций...\n")

    if not transactions:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Программа: Всего банковских операций в выборке: {len(transactions)}\n")

    for t in transactions:
        # Форматируем основные данные
        date = get_date(t.get("date", ""))
        description = t.get("description", "Операция")

        # Форматируем отправителя и получателя
        from_ = get_mask_card_number(t.get("from", "")) if t.get("from") else "N/A"
        to_ = get_mask_account(t.get("to", "")) if t.get("to") else "N/A"

        # Форматируем сумму и валюту
        amount = t.get("amount", 0)
        currency = t.get("currency_name", "руб.")

        print(f"{date} {description}")
        if from_ != "N/A":
            print(f"{from_} -> {to_}")
        else:
            print(f"{to_}")
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    data = select_file()
    filtered_data = filter_status(data)
    sorted_data = sorting_question(filtered_data)
    print_transactions(sorted_data)
