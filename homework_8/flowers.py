from dataclasses import dataclass

@dataclass
class Flower:
    name: str
    price: float
    life_time: float
    def __init__(self, name: str, price: float, life_time: float):
        if price < 0:
            raise ValueError("Стоимость не может быть отрицательной!")
        if life_time <= 0:
            raise ValueError("Время жизни цветка не может быть меньше 0!")
        self.name = name
        self.price = price
        self.life_time = life_time

@dataclass
class Rose(Flower):
    def __init__(self, price: float, life_time: float = 7):
        super().__init__(name = "Роза", price = price, life_time = life_time)

@dataclass
class Chrysanthemum(Flower):
    def __init__(self, price: float, life_time: float = 10):
        super().__init__(name = "Хризантема", price = price, life_time = life_time)

@dataclass
class Lilly(Flower):
    def __init__(self, price: float, life_time: float = 5):
        super().__init__(name = "Лиллия", price = price, life_time = life_time)