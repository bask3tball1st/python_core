class InvalidTestStatusError(Exception):
    pass

def check_status(status):
    if status not in ["PASS", "FAIL", "SKIP"]:
        raise InvalidTestStatusError(f"Неизвестный статус теста: {status}")
    else:
        print(f"Верный статус: {status}")

if __name__ == "__main__":
    try:
        input_status = input("Введите статус теста:").upper()
        check_status(input_status)
    except InvalidTestStatusError as err:
        print("Ошбика!", err)