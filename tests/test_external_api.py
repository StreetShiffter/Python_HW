import json
import unittest
from unittest.mock import patch, MagicMock
from src.external_api import currency_exchange, transaction_info

@patch('requests.get')
def test_currency_exchange_success(mock_get):
    # Настраиваем mock-объект, чтобы возвращать статус 200 и JSON-ответ
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'result': 100} # Пример результата конвертации
    mock_get.return_value = mock_response

    result = currency_exchange('USD', 'RUB', 10)

    # Простой assert для проверки результата
    assert result == {'result': 100}, "Expected result to be {'result': 100}"


