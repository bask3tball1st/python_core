from functools import wraps
import random

def retry(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(count):
                print("Попытка №", attempt + 1)
                result = func(*args, **kwargs)
                print("Функция вернула", result)
                if result is True:
                    print("Программа завершена!")
                    return result
            return result
        return wrapper
    return decorator

@retry(3)
def random_result_func():
    return random.choice([True, False])

random_result_func()