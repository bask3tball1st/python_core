import random

def choice_unique_tests(tests_list, number):
    unique_tests = random.sample(tests_list, number)
    unique_tests_dict= dict.fromkeys(unique_tests, "NOT STARTED")
    for key, value in unique_tests_dict.items():
        unique_tests_dict[key] = random.choice(["PASS", "FAIL", "SKIP"])
    return unique_tests_dict

def print_results(results_list):
    for key, value in results_list.items():
        print(key + ": " + str(value))

tests = [
"test_login",
"test_logout",
"test_registration",
"test_profile",
"test_payment",
"test_search"
]

test_length = len(tests)
n = int(input("Введите количество тестов, которое необходимо запустить: "))
if n <= test_length and n != 0:
    print("Результаты проведенных тестов:")
    print_results(choice_unique_tests(tests, n))
else:
    print("Ошбика! Введенное число превышает количество доступных тестов!")