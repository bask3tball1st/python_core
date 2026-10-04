from functools import wraps

def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Перед вызовом функции")
        print("Имя функции", func.__name__)
        result = func(*args, **kwargs)
        print("Функция завершила выполнение!")
        print("Результат:", result)
        return result
    return wrapper

@log_test
def calculate(a, b):
    return a + b

calculate(10, 20)