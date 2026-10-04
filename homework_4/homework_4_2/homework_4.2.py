try:
    with open('file_4.2.txt', 'r') as f:
        even_numbers = []
        odd_numbers = []
        for line in f:
            number = int(line.strip())
            if number % 2 == 0:
                even_numbers.append(number)
            else:
                odd_numbers.append(number)
    with open('file_4.2.1.txt', 'w') as file1:
        for number in even_numbers:
            file1.write(str(number) + "\n")
        print("Файл с четными числами записан!")
    with open('file_4.2.2.txt', 'w') as file2:
        for number in odd_numbers:
            file2.write(str(number) + "\n")
        print("Файл с нечетными числами записан!")
except FileNotFoundError:
    print("Файл не найден!")
except ValueError:
    print("Ошбика! Заполните файл целыми числами!")
    with open('file_4.2.1.txt', 'w') as file1:
        file1.write("")
    with open('file_4.2.2.txt', 'w') as file2:
        file2.write("")