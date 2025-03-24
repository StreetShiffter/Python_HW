import pytest


@pytest.fixture
def info_string_card()-> str:
    return "1234 5678 9876 5432"


@pytest.fixture
def info_string_score()-> str:
    return "1234 5678 9876 5432 8596 1"


@pytest.fixture
def info_name_card()-> str:
    return "Visa Platinum 8990922113665229"


@pytest.fixture
def info_name_score()-> str:
    return "Счет 899092211366522986742"


@pytest.fixture
def info_date()-> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def info_state()-> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def info_state_right()-> tuple:
    info_state = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    result = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    return info_state, result


@pytest.fixture
def sort_data_right()-> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def same_data()-> list[dict]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
        {"id": 2, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
        {"id": 4, "state": "CANCELED", "date": "2023-01-01T10:00:00"},
        {"id": 5, "state": "CANCELED", "date": "2023-01-01T10:00:00"},
    ]
