class CreditCard:
    def __init__(self, account_number, balance):
        if account_number <= 0:
            raise ValueError("Номер счета должен быть положительным!")
        else:
            self.__account_number = account_number
        if balance <= 0:
            raise ValueError("Начальный баланс должен быть положительным!")
        else:
            self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма для пополнения должна быть больше 0!")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должны быть больше 0!")
        if amount > self.__balance:
            raise ValueError(f"Невозможно снять указанную сумму с карты {self.__account_number}! Недостаточно средств!")
        self.__balance -= amount

    def show_info(self):
        print("Номер счета:", self.__account_number)
        print("Текущий баланс:", self.__balance)

try:
    card1 = CreditCard(1, 100)
    card2 = CreditCard(2, 200)
    card3 = CreditCard(3, 300)

    card1.deposit(100)
    card2.deposit(200)
    card3.withdraw(300)
    card1.show_info()
    card2.show_info()
    card3.show_info()
except ValueError as e:
    print("Ошибка!", e)