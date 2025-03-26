import pytest
from src.generators import filter_by_currency

def test_filter_by_currency(list_gen: tuple[list[dict], list[dict]]) -> None:
    test, result = list_gen
    usd_transactions = list(filter_by_currency(test, "USD"))
    assert usd_transactions == result

@pytest.mark.parametrize("state, expected", [
    ("USD", [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }, {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }]),
    ("EUR", [{
        "id": 223456789,
        "state": "EXECUTED",
        "date": "2020-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "500.00",
            "currency": {
                "name": "EUR",
                "code": "EUR"
            }
        },
        "description": "Перевод между счетами",
        "from": "Счет 12345678901234567890",
        "to": "Счет 09876543210987654321"
    }])
])
def test_filter_by_currency_unique(list_gen_data: list[dict], state: str, expected: list[dict]) -> None:
    test = list_gen_data
    testing_transactions = list(filter_by_currency(test, state))
    assert testing_transactions == expected

def test_rise_filter_by_currency()-> None:
    transactions = []
    with pytest.raises(TypeError):
        filter_by_currency(transactions)
