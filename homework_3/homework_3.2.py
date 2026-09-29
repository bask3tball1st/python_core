def print_report(test_cases_list, status_list):
    final_report = zip(test_cases_list, status_list)
    count_fail_status = 0
    count_pass_status = 0
    count_skip_status = 0
    for test_case, status in final_report:
        print(test_case + " — " + status)
        if status == "FAIL":
            count_fail_status += 1
        elif status == "PASS":
            count_pass_status += 1
        elif status == "SKIP":
            count_skip_status += 1
    print("Количество успешных тестов: " + str(count_pass_status))
    print("Количество неуспешных тестов: " + str(count_fail_status))
    print("Количество пропущенных тестов: " + str(count_skip_status))
    if count_fail_status > 0:
        print("Тестовый запуск неуспешен!")
    else:
        print("Тестовый запуск успешен!")

test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]
print_report(test_cases, statuses)