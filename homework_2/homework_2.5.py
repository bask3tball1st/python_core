n = int(input("Введите количество автотестов: "))
test_results = {"Pass": 0, "Fail": 0, "Skip": 0}

for counts in range(n):
    status = input("Введите результат теста: ")
    if status == "Pass":
        test_results["Pass"] += 1
    elif status == "Fail":
        test_results["Fail"] += 1
    elif status == "Skip":
        test_results["Skip"] += 1

print("Итоговая статистика:\n" + str(test_results))
if test_results["Fail"] > 0:
    print("В прохождении присутсвуют упавшие тесты!")
else:
    print("Все тесты успешно пройдены!")