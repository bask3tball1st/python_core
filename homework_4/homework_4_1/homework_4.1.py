try:
    with open('file_4.1.txt', 'r') as f:
        number = []
        for line in f:
            number.append(int(line.strip()))
        if len(number) < 3:
            print("Ошбика! В файле меньше 3-х чисел!")
        else:
            print(number[0], number[1], number[-2], number[-1])
except FileNotFoundError:
    print("Файл не найден!")
except ValueError:
    print("Ошбика! Заполните файл числами!")
