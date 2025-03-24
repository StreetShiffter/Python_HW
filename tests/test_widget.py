import pytest
from src.widget import mask_account_card, get_date


def test_mask_account_card(info_name_card: str)-> None:
    assert mask_account_card(info_name_card) == ("Visa Platinum", "8990922113665229")
    assert mask_account_card(info_name_card) != ("Visa Platinum 8990922113665229")


def test_mask_account_score(info_name_score: str)-> None:
    assert mask_account_card(info_name_score) != ("Счет 899092211366522986742")
    assert mask_account_card(info_name_score) == ("Счет", "899092211366522986742")


@pytest.mark.parametrize(
    "input_num, result_num",
    [
        ("Mastercard 4563965874125870", ("Mastercard", "4563965874125870")),
        ("Мир 2202589647103301", ("Мир", "2202589647103301")),
        ("Счет 854773004938123374589025", ("Счет", "854773004938123374589025")),
    ],
)
def test_several_number(input_num: str, result_num: tuple)-> None:
    assert mask_account_card(input_num) == result_num


@pytest.mark.parametrize(
    "input_string",
    [
        "2023658 8990922113665229",  # Некорректный ввод (небуквенное значение)
        "!@#$%^&*()_+",  # Специальные символы
    ],
)
def test_check_name(input_string: str)-> None:
    with pytest.raises(ValueError):
        mask_account_card(input_string)


@pytest.mark.parametrize(
    "input_string",
    [
        "Visa номер_карты",  # Некорректный ввод (нецифровое значение)
        "MasterCard 1234abcd",  # Нецифровое значение
    ],
)
def test_check_number(input_string: str)-> None:
    with pytest.raises(ValueError):
        mask_account_card(input_string)


def test_date(info_date: str)-> None:
    assert get_date(info_date) == "11.03.2024"
    assert get_date(info_date) != "11.03.24"


@pytest.mark.parametrize(
    "input_date, expected_output",
    [
        (None, None),
        ("", None),
        ("invalid_string", None),
        ("2024-03-11T02:26:18.6714079", None),
        ("24-3-1T2:6:8.7", None),
        ("2024-03-11T2:26:18", None),
        ("2024-03-11T02:26:18.67140798", None),
    ],
)
def test_check_date(input_date: str, expected_output: tuple )-> None:
    if expected_output is None:
        with pytest.raises((TypeError, ValueError)):
            get_date(input_date)
    else:
        assert get_date(input_date) == expected_output
