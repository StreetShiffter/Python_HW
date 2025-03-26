import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_right(info_state_right: tuple[list[dict], list[dict]]) -> None:
    data, result = info_state_right
    assert filter_by_state(data) == result


def test_filter_by_state(info_state: list[dict]) -> None:
    test_1 = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    test_2 = [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    assert filter_by_state(info_state, "EXECUTED") == test_1
    assert filter_by_state(info_state, "CANCELED") == test_2
    assert filter_by_state(info_state, "EXECUTED") != test_2
    assert filter_by_state(info_state, "CANCELED") != test_1
    assert filter_by_state(info_state, "OBJECTIONABLE") == []


@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ],
     ),
    ("CANCELED", [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ],
     ),
    ("UNKNOWN", []),
    ("", [])
]
                         )
def test_filter_by_state_check(info_state: list[dict], state: str, expected: list[dict]) -> None:
    assert filter_by_state(info_state, state) == expected


def test_sort_date_right(sort_data_right: list[dict]) -> None:
    result = sort_by_date(sort_data_right, True)
    expected_output = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert result == expected_output


def test_sort_date_wrong(sort_data_right: list[dict]) -> None:
    result = sort_by_date(sort_data_right, False)
    expected_output = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert result == expected_output


def test_same_date(same_data: list[dict]) -> None:
    result = sort_by_date(same_data, True)
    test_list = [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
        {"id": 2, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
        {"id": 4, "state": "CANCELED", "date": "2023-01-01T10:00:00"},
        {"id": 5, "state": "CANCELED", "date": "2023-01-01T10:00:00"},
    ]
    assert result == test_list


def test_sort_date_invalid_format() -> None:
    data_with_invalid_dates = [
        {"id": 1, "state": "EXECUTED", "date": "invalid-date"},
        {"id": 2, "state": "EXECUTED", "date": ""},
        {"id": 3, "state": "EXECUTED", "date": None},
    ]
    with pytest.raises(TypeError):
        sort_by_date(data_with_invalid_dates)


def test_sort_date_missing_date() -> None:
    data_with_missing_dates = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "EXECUTED", "date": "2019-01-01T00:00:00.000000"},
    ]

    with pytest.raises(TypeError):
        sort_by_date(data_with_missing_dates)


def test_sort_date_valid_format() -> None:
    data_with_invalid_dates = [
        {"id": 1, "state": "EXECUTED", "date": "invalid-date"},
        {"id": 2, "state": "EXECUTED", "date": ""},
        {"id": 3, "state": "EXECUTED", "date": None},
        {"id": 4, "state": "EXECUTED", "date": "not-a-date"}
    ]
    with pytest.raises(TypeError):
        sort_by_date(data_with_invalid_dates)
