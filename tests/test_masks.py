import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "input_num, result_num",
    [
        ("1234 5678 9876 5432", "1234 56** **** 5432"),
        ("9876 5432 1023 4567", "9876 54** **** 4567"),
        ("4276 0058 5432 1023", "4276 00** **** 1023"),
    ],
)
def test_mask_several(input_num: str, result_num: str)-> None:
    assert get_mask_card_number(input_num) == result_num


@pytest.mark.parametrize(
    "input_string",
    [
        "Номер карты",  # Некорректный ввод (нечисловое значение)
        "!@#$%^&*()_+",  # Специальные символы
    ],
)
def test_invalid_card_number(input_string: str)-> None:
    with pytest.raises(ValueError):
        get_mask_card_number(input_string)


def test_mask_card_number(info_string_card: str)-> None:
    assert get_mask_card_number(info_string_card) == "1234 56** **** 5432"
    assert get_mask_card_number(info_string_card) != "1234 567* **** *432"


def test_mask_card_score(info_string_score: str)-> None:
    assert get_mask_card_number(info_string_score) == "12345678987******5961"
    assert get_mask_card_number(info_string_score) != "12345678987 ****** 5961"


@pytest.mark.parametrize(
    "input_num, result_num",
    [
        ("9876 5432 1023 4567", "** 4567"),
        ("4276 0058 5432 1023", "** 1023"),
    ],
)
def test_mask_account_several(input_num: str, result_num: str)-> None:
    assert get_mask_account(input_num) == result_num


@pytest.mark.parametrize("try_string", ["Номер карты", "!@#$%^&*()_+", "123"])  # Длина номера
def test_invalid_account_number(try_string: str)-> None:
    with pytest.raises(ValueError):
        get_mask_account(try_string)


def test_mask_account_number(info_string_card: str)-> None:
    assert get_mask_account(info_string_card) == "** 5432"
    assert get_mask_account(info_string_card) != "** *432"