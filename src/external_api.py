import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API")




def currency_exchange(output_code: str, input_code: str, amount: int | float) -> dict:
    """Функция конвертации любой валюты"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={input_code}&from={output_code}&amount={amount}"

    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Возвращаем JSON-ответ
    else:
        response.raise_for_status()  # Генерируем исключение для ошибок


def transaction_info(transaction: list[dict]) -> float:
    """Вывод суммы транзакции"""
    for item in transaction:
        if item["operationAmount"]["currency"]["code"] == "RUB":
            money = float(item["operationAmount"]["amount"])
            return money

        elif item["operationAmount"]["currency"]["code"] != "RUB":
            convert = item["operationAmount"]["amount"]
            input = item["operationAmount"]["currency"]["code"]
            output = "RUB"
            result_dict = currency_exchange(input, output, convert)
            money = result_dict["result"]

            return float(money)
        else:
            return 0.0


transaction = [

{
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]

if __name__ == "__main__":

    result=transaction_info(transaction)
    print(type(result))