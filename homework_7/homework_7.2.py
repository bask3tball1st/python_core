class ATM:
    def __init__(self, banknote_100 = 0, banknote_50 = 0, banknote_20 = 0):
        if banknote_20 < 0 or banknote_50 < 0 or banknote_100 < 0:
            raise ValueError("Купюры не добавлены в банкомат! Введите корректное количество купюр!")
        self.__banknotes = {20: banknote_20, 50: banknote_50, 100: banknote_100}

    def add_money(self, banknote_100, banknote_50, banknote_20):
        if banknote_20 < 0 or banknote_50 < 0 or banknote_100 < 0:
            raise ValueError("Купюры не добавлены в банкомат! Введите корректное количество купюр!")
        self.__banknotes[20] += banknote_20
        self.__banknotes[50] += banknote_50
        self.__banknotes[100] += banknote_100

    def show_info(self):
        print("-----------------")
        print("Банкнота 100:", self.__banknotes[100])
        print("Банкнота 50:", self.__banknotes[50])
        print("Банкнота 20:", self.__banknotes[20])
        print("-----------------")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше 0!")
        total_amount = self.__banknotes[20] * 20 + self.__banknotes[50] * 50 + self.__banknotes[100] * 100
        if amount > total_amount or amount % 10 != 0:
            print("Банкомат не может выдать данную сумму!")
            return False
        max_bills100 = min(amount // 100, self.__banknotes[100])
        for temp_bills100 in range(max_bills100, -1, -1):
            temp_amount = amount - temp_bills100 * 100
            max_bills50 = min(temp_amount // 50, self.__banknotes[50])
            for temp_bills50 in range(max_bills50, -1, -1):
                temp_amount_after = temp_amount - temp_bills50 * 50
                if temp_amount_after % 20 == 0:
                    temp_bills20 = temp_amount_after // 20
                    if temp_bills20 <= self.__banknotes[20]:
                        self.__banknotes[20] -= temp_bills20
                        self.__banknotes[50] -= temp_bills50
                        self.__banknotes[100] -= temp_bills100
                        print("Операция успешно проведена!")
                        print("Выдано 100:", temp_bills100)
                        print("Выдано 50:", temp_bills50)
                        print("Выдано 20:", temp_bills20)
                        return True
        print("Невозможно выдать данную сумму!")
        return False

try:
    atm = ATM(1, 4, 4)
    atm.add_money(0, 10, 5)
    atm.add_money(5, 0, 0)
    atm.show_info()
    atm.withdraw(230)
    atm.withdraw(720)
    atm.withdraw(310)
    atm.withdraw(300)
    atm.show_info()
except ValueError as e:
    print(e)