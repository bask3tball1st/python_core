import random

def generate_login():
    login = random.randint(100000, 999999)
    return login

def generate_age():
    age = random.randint(18, 90)
    return age

def generate_status():
    status = random.choice(["ACTIVE", "INACTIVE", "BLOCKED"])
    return status

def generate_user():
    return {
        "user_login": generate_login(),
        "user_age": generate_age(),
        "user_status": generate_status()
    }