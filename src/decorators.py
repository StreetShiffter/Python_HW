import sys
from functools import wraps


def log(filename=None):
    """Декоратор для логирования выполнения функций"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Определяем куда писать логи
            output = open(filename, 'a', encoding='utf-8') if filename else sys.stdout

            try:
                # Выполняем функцию
                result = func(*args, **kwargs)
                # Логируем успех
                print(f"{func.__name__} ok", file=output)
                return result
            except Exception as e:
                # Логируем ошибку
                print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}",
                      file=output)
                raise
            finally:
                if filename:
                    output.close()

        return wrapper

    return decorator