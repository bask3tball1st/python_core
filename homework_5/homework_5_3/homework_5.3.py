try:
    repeat_count = int(input("Введите количество повторных запусков: "))
    if repeat_count < 0 or repeat_count > 5:
        raise ValueError(f"Количество повторных превышает диапазон от 0 до 5! Ваше количество: {repeat_count}")
    test_timeout = float(input("Введите значение таймаута: "))
    if test_timeout < 0:
        raise ValueError("Таймаут должен быть положительным!")
except ValueError as err:
    print(f"Ошбика! {err}")