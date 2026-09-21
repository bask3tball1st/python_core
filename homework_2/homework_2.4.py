secret_count = 37
count = 0
while count != secret_count:
    count = int(input("Enter the number: "))
    if count == secret_count:
        print("You successfully guessed the number")
        break
    elif count > secret_count:
        print("You guessed too high")
    elif count < secret_count:
        print("You guessed too low")