for numbers in range(1,31):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("BugTest")
    elif numbers % 5 == 0:
        print("Test")
    elif numbers % 3 == 0:
        print("Bug")
    else:
        print(numbers)