from dataclasses import dataclass

@dataclass
class Accessory:
    name: str
    price: float
    def __init__(self, name, price):
        if price < 0:
            raise ValueError("Стоимость аксессуара не может быть отрицательной!")
        self.name = name
        self.price = price

@dataclass
class Tape(Accessory):
    def __init__(self, price: float):
        super().__init__(name = "Ленточка", price = price)

@dataclass
class Card(Accessory):
    def __init__(self, price: float):
        super().__init__(name = "Открытка", price = price)

@dataclass
class Paper(Accessory):
    def __init__(self, price: float):
        super().__init__(name = "Крафтовая бумага", price = price)