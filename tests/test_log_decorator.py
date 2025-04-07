import pytest
from src.decorators import log


def test_console_log_success(capsys):
    """Тест успешного выполнения с выводом в консоль"""

    @log()
    def add(a, b):
        return a + b

    result = add(1, 2)
    assert result == 3

    captured = capsys.readouterr()
    assert captured.out == "add ok\n"
    assert captured.err == ""


def test_console_log_error(capsys):
    """Тест ошибки с выводом в консоль"""

    @log()
    def div(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    captured = capsys.readouterr()
    assert "div error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0)" in captured.out


def test_file_log_success(tmp_path):
    """Тест успешного выполнения с выводом в файл"""
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    result = multiply(3, 4)
    assert result == 12

    # Проверяем содержимое файла
    with open(log_file, 'r', encoding='utf-8') as f:
        content = f.read()
        assert content == "multiply ok\n"


def test_file_log_error(tmp_path):
    """Тест ошибки с выводом в файл"""
    log_file = tmp_path / "error.log"

    @log(filename=str(log_file))
    def fail():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        fail()

    # Проверяем содержимое файла
    with open(log_file, 'r', encoding='utf-8') as f:
        content = f.read()
        assert "fail error: ValueError" in content
        assert "Inputs: (), {}" in content


def test_function_metadata_preserved():
    """Тест сохранения метаданных функции"""

    @log()
    def sample(a: int, b: int = 1) -> int:
        """Тестовая функция"""
        return a + b

    assert sample.__name__ == "sample"
    assert sample.__doc__ == "Тестовая функция"
    assert sample.__annotations__ == {'a': int, 'b': int, 'return': int}
