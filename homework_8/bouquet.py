from dataclasses import dataclass
from homework_8.accessories import Accessory
from homework_8.flowers import Flower

@dataclass
class Bouquet:
    def __init__(self):
        self._flowers: list[Flower] = []
        self._accessories: list[Accessory] = []

    def add_flower(self, flower: Flower):
        self._flowers.append(flower)

    def add_accessory(self, accessory: Accessory):
        self._accessories.append(accessory)

    def total_price(self):
        flowers_price = sum(fl.price for fl in self._flowers)
        accessories_price = sum(a.price for a in self._accessories)
        return flowers_price + accessories_price

    def average_withering_time(self):
        if not self._flowers:
            return None
        return sum(fl.life_time for fl in self._flowers) / len(self._flowers)

    def sort_flowers_by_price(self):
        return sorted(self._flowers, key=lambda fl: fl.price)

    def contains_flower(self, name: str):
        for fl in self._flowers:
            if fl.name.lower() == name.lower():
                print(f"Цветок {fl.name.lower()} присутсвует в букете!")
                return True
        print(f"Цветка {name.lower()} в букете нет!")
        return False

    def print_bouquet(self):
        print("Букет состоит из:")
        for fl in self._flowers:
            print(f"\t{fl.name}: {fl.price}")
        for accessory in self._accessories:
            print(f"\t{accessory.name}: {accessory.price}")