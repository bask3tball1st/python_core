secret_number = 37
guessed_number = 0
count = 0
while guessed_number != secret_number:
    guessed_number = int(input("Enter the number: "))
    count += 1
    if guessed_number == secret_number:
        print("You successfully guessed the number! Attempts: " + str(count))
        break
    elif guessed_number > secret_number:
        print("You guessed too high")
    elif guessed_number < secret_number:
        print("You guessed too low")