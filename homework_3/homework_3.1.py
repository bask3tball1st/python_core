def get_test_statistics(results):
    res_count = dict.fromkeys(results, 0)
    for i in range(len(results)):
        if results[i] == "PASS":
            res_count[results[i]] += 1
        elif results[i] == "FAIL":
            res_count[results[i]] += 1
        elif results[i] == "SKIP":
            res_count[results[i]] += 1
    return res_count

def print_results(results):
    for key, value in results.items():
        print(key + ": " + str(value))

test_results = input("Введите результаты запуска тестов через пробел: ")
test_results = list(map(str, test_results.split()))
produced_result = get_test_statistics(test_results)
total = sum(produced_result.values())
success_percentage = round((produced_result["PASS"] / total) * 100, 1)
print("Всего тестов: " + str(total))
print_results(produced_result)
print(str(success_percentage) + "%")
