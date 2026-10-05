import json
from functools import reduce

def counting_duration(count, auto_tests_dict):
    return count + auto_tests_dict["duration"]

def results_list(json_data):
    for auto_test in json_data:
        if "name" not in auto_test or "status" not in auto_test or "duration" not in auto_test:
            raise ValueError("Отсутсвует обязательное поле!")
    passed_tests = [test["name"] for test in json_data if test["status"] == 'PASS']
    failed_tests = list(filter(lambda test: test["status"] == "FAIL", json_data))
    skipped_tests = list(filter(lambda test: test["status"] == "SKIP", json_data))
    total_count_tests = len(json_data)
    failed_tests_name = list(map(lambda test: test["name"], failed_tests))
    max_duration_test = max(json_data, key=lambda test: test["duration"])
    total_duration = reduce(counting_duration, json_data, 0.0)
    results = [
        {
            "Total number of tests": total_count_tests,
            "Number of tests passed": len(passed_tests),
            "Number of tests failed": len(failed_tests),
            "Number of tests skipped": len(skipped_tests),
            "List of failed tests": failed_tests_name,
            "Max duration test": { "name": max_duration_test["name"], "duration": max_duration_test["duration"] },
            "Total duration": total_duration,
        }
    ]
    return results

def record_json(result_data):
    try:
        with open("result.json", "w") as result_file:
            json.dump(result_data, result_file, indent=4)
    except IOError as error:
        print("Ошибка записи в файл:", error)

if __name__ == "__main__":
    try:
        with open("tests.json", "r") as read_file:
            data = json.load(read_file)
        record_json(results_list(data))
    except FileNotFoundError as err:
        print("Ошибка:", err)
    except json.JSONDecodeError as err:
        print("Невалидный JSON файл!")
        print("Ошибка:", err)
    except ValueError as err:
        print("Ошибка!", err)