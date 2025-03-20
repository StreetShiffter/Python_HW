import pytest
from src.widget import mask_account_card, get_date

def test_mask_account_card(info_name_card):
    assert mask_account_card(info_name_card) == ("Visa Platinum", "8990922113665229")
    assert mask_account_card(info_name_card) != ("Visa Platinum 8990922113665229")


def test_mask_account_score(info_name_score):
    assert mask_account_card(info_name_score) != ("Счет 899092211366522986742")
    assert mask_account_card(info_name_score) == ("Счет", "899092211366522986742")


@pytest.mark.parametrize('input_num, result_num',[
        ("Mastercard 4563965874125870", ("Mastercard", "4563965874125870")),
        ("Мир 2202589647103301", ("Мир", "2202589647103301")),
        ("Счет 854773004938123374589025", ("Счет", "854773004938123374589025"))
    ])
def test_several_number(input_num, result_num):
    assert mask_account_card(input_num) == result_num


@pytest.mark.parametrize("input_string", [
    "2023658 8990922113665229", # Некорректный ввод (небуквенное значение)
    "!@#$%^&*()_+",             # Специальные символы
])
def test_check_name(input_string):
    with pytest.raises(ValueError):
        mask_account_card(input_string)

@pytest.mark.parametrize("input_string", [
    "Visa номер_карты",            # Некорректный ввод (нецифровое значение)
    "MasterCard 1234abcd",        # Нецифровое значение
])
def test_check_number(input_string):
    with pytest.raises(ValueError):
        mask_account_card(input_string)


def test_date(info_date):
    assert get_date(info_date) == "11.03.2024"
    assert get_date(info_date) != "11.03.24"


@pytest.mark.parametrize('input_date, result_date', [
    ("2024-03-15T02:26:18.671407", "15.03.2024"),
    ("2004-05-10T02:20:17.273404", "10.05.2004")
])
def test_date_several(input_date, result_date):
    assert get_date(input_date) == result_date
