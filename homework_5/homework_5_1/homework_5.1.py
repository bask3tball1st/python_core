from functools import reduce

def read_auto_tests():
    auto_tests_dict = []
    with open("autotests.txt", "r") as file:
        for line in file:
            part_line = line.strip().split()
            if len(part_line) == 3:
                name, status, duration = part_line
                auto_tests_dict.append({
                    "name": name,
                    "status": status,
                    "duration": float(duration)
                })
            else:
                continue
    return auto_tests_dict

def print_results(auto_tests_dict):
    failed_tests = list(filter(lambda test: test["status"] == "FAIL", auto_tests))
    failed_tests_name = list(map(lambda test: test["name"], failed_tests))
    total_duration = reduce(counting_duration, auto_tests, 0.0)
    passed_tests = [test["name"] for test in auto_tests if test["status"] == 'PASS']
    print("Количество успешных тестов: ", len(passed_tests))
    print("Количество упавших тестов: ", len(failed_tests))
    print("Количетсво пропущенных тестов: ", len(auto_tests_dict) - (len(failed_tests) + len(passed_tests)))
    print("Список успешно пройденных тестов: ", ", ".join(passed_tests))
    print("Список упавших тестов: ", ", ".join(failed_tests_name))
    print("Общее время выполнения всех тестов: ", total_duration)

def counting_duration(count, auto_tests_dict):
    return count + auto_tests_dict["duration"]

if __name__ == "__main__":
    auto_tests = read_auto_tests()
    print_results(auto_tests)