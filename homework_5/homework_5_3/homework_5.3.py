def check_correctness(count, timeout):
    try:
        if count < 0 or count > 5:
            raise ValueError(f"Количество повторных запусков превышает диапазон от 0 до 5! Ваше количество: {count}")
        elif timeout <= 0:
            raise ValueError("Таймаут должен быть положительным!")
        else:
            print("Все данные введены корректно!")
    except ValueError as err:
        print(f"Ошбика! {err}")

#repeat_count = int(input("Введите количество повторных запусков: "))
#test_timeout = float(input("Введите значение таймаута: "))
check_correctness(4, 3)
check_correctness(3, -1)
check_correctness(7, 3)