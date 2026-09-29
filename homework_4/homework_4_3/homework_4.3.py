try:
    with open('file_4.3.txt', 'r') as f:
        numbers = []
        for line in f:
            numbers.append(float(line.strip())**2)
    with open(r'file_4.3.txt', 'w') as f:
        for number in numbers:
            f.write(str(number) + "\n")
        print("Файл успешно перезаписан!")
except FileNotFoundError:
    print("Файл не найден!")
except ValueError:
    print("Ошбика! Заполните файл вещественными числами!")
