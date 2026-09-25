for user in range(1,21):
    if user % 5 == 0:
        continue
    elif user == 18:
        break
    else:
        print("Start testing user " + str(user))