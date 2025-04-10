import json
import unittest
from unittest.mock import patch, mock_open
from src.utils import read_file



@patch("builtins.open", new_callable=mock_open, read_data='[{"key": "value"}]')
def test_read_file_success(mock_file):
    result = read_file("dummy_path.json")
    assert result == [{"key": "value"}]

# Второй тест
@patch("builtins.open", new_callable=mock_open, read_data='not a json')
def test_read_file_invalid_json(mock_file):
    result = read_file("dummy_path.json")
    assert result == []

# Третий тест
@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_file_not_found(mock_file):
    result = read_file("dummy_path.json")
    assert result == []
