correct_password = "Python123"
count = 0
for attempt in range(3):
    password = input("Please enter your password: ")
    if password == correct_password:
        print("You have successfully logged in!")
        break
    else:
        count += 1
if count == 3:
    print("Access denied!")