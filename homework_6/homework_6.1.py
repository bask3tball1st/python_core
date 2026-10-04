def read_results():
    with open("test_results.txt","r") as f:
        data = f.read().split()
        results = []
        for res in data:
            results.append(res.upper())
    return results

def count_pass_tests(results):
    if not results:
        return 0
    else:
        if results[0] == "PASS":
            return 1 + count_pass_tests(results[1:])
        else:
            return 0 + count_pass_tests(results[1:])

if __name__ == "__main__":
    test_results = read_results()
    count = count_pass_tests(test_results)
    print("Количество тестов со статусом PASS:", count)