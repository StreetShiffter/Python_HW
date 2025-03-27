import pytest
from src.generators import card_number_generator

# def test_filter_by_currency(list_gen: tuple[list[dict], list[dict]]) -> None:
#     test, result = list_gen
#     usd_transactions = list(filter_by_currency(test, "USD"))
#     assert usd_transactions == result
#
# @pytest.mark.parametrize("state, expected", [
#     ("USD", [{
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {
#             "amount": "9824.07",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702"
#     }, {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {
#             "amount": "9824.07",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702"
#     }]),
#     ("EUR", [{
#         "id": 223456789,
#         "state": "EXECUTED",
#         "date": "2020-04-04T23:20:05.206878",
#         "operationAmount": {
#             "amount": "500.00",
#             "currency": {
#                 "name": "EUR",
#                 "code": "EUR"
#             }
#         },
#         "description": "Перевод между счетами",
#         "from": "Счет 12345678901234567890",
#         "to": "Счет 09876543210987654321"
#     }])
# ])
# def test_filter_by_currency_unique(list_gen_data: list[dict], state: str, expected: list[dict]) -> None:
#     test = list_gen_data
#     testing_transactions = list(filter_by_currency(test, state))
#     assert testing_transactions == expected
#
# def test_rise_filter_by_currency()-> None:
#     transactions = []
#     with pytest.raises(ValueError):
#         next(filter_by_currency(transactions, "USD"))
#
#
# def test_transaction_descriptions(right_description) -> None:
#     expected = [
#         "Перевод организации",
#         "Перевод со счета на счет",
#         "Отсутствует описание"
#     ]
#     iterations = list(transaction_descriptions(right_description))
#     assert iterations == expected
#
#
# def test_rise_transaction_descriptions() -> None:
#     list_none = []
#     with pytest.raises(ValueError):
#         next(transaction_descriptions(list_none))


def test_card_number_generator(generator_card)-> list[str]:
    result = generator_card
    start = "1"
    stop = "5"
    assert list(card_number_generator(int(start), int(stop))) == result

@pytest.mark.parametrize(
    'start, stop, expected',[
        ('2', '6', [
            '0000 0000 0000 0002',
            '0000 0000 0000 0003',
            '0000 0000 0000 0004',
            '0000 0000 0000 0005',
            '0000 0000 0000 0006'
        ]),
        ('9', '13', [
            '0000 0000 0000 0009',
            '0000 0000 0000 0010',
            '0000 0000 0000 0011',
            '0000 0000 0000 0012',
            '0000 0000 0000 0013'
        ])
    ]
)

def test_card_number_generator_check(start: int, stop: int, expected: list[str]) -> None:
    start_int = int(start)
    stop_int = int(stop)
    initial = list(card_number_generator(start_int, stop_int))
    assert initial == expected

def  test_card_number_generator_raises():
    with pytest.raises(ValueError):
        test_1 = list(card_number_generator(5, 2))
        test_2 = list(card_number_generator(10, 2))
        test_3 = list(card_number_generator(3, 'five'))
        assert test_1
        assert test_2
        assert test_3



