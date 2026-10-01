import json

def print_users(users_dict):
    print("Информация о пользователях")
    for user in users_dict:
        if "login" not in user or "password" not in user or "is_authorize" not in user:
            raise ValueError(f"Отсутсвует обязательное поле у пользователя {user["login"]}!")
        print("---------------------------")
        print("Пользователь", user["login"])
        print("Логин:", user["login"])
        print("Пароль:", user["password"])
        print("Статус авторизации:", user["is_authorize"])

try:
    with open("users.json", "r") as read_file:
        data = json.load(read_file)
    print_users(data)
except FileNotFoundError as err:
    print("Ошибка:", {err})
except json.JSONDecodeError as err:
    print("Невалидный JSON файл!")
    print("Ошибка:", err)
except ValueError as err:
    print("Ошибка!", err)