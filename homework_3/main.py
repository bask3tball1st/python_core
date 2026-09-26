import test_data

def print_users(users_list):
    for user in users_list:
        print(user)

def status_stats(users_list):
    status = dict.fromkeys(["ACTIVE", "INACTIVE", "BLOCKED"], 0)
    for user in users_list:
        status[user["user_status"]] += 1
    return status


def main():
    user_counts = int(input("Введите количество пользователей: "))
    users = []
    if user_counts > 0:
        for i in range(user_counts):
            users.append(test_data.generate_user())
        print_users(users)
        print("Статистика пользователей по статусу:")
        print(status_stats(users))
    else:
        print("Количество пользователей не может быть отрицательным или равным нулю!")

if __name__ == "__main__":
    main()