from homework_8 import bouquet
from homework_8.accessories import Tape
from homework_8.accessories import Card
from homework_8.accessories import Paper
from homework_8.flowers import Rose
from homework_8.flowers import Chrysanthemum
from homework_8.flowers import Lilly

if __name__ == '__main__':
    rose1 = Rose(price = 200)
    rose2 = Rose(price = 170, life_time = 5)
    lilly = Lilly(price = 100, life_time = 5)
    chrysanthemum = Chrysanthemum(price = 300, life_time = 10)

    tape = Tape(price = 20)
    card = Card(price = 10)
    kraft_paper = Paper(price = 30)

    bouquet1 = bouquet.Bouquet()
    bouquet1.add_flower(rose1)
    bouquet1.add_flower(lilly)
    bouquet1.add_accessory(card)
    bouquet1.add_accessory(tape)

    bouquet2 = bouquet.Bouquet()
    bouquet2.add_flower(rose2)
    bouquet2.add_flower(chrysanthemum)
    bouquet2.add_accessory(kraft_paper)

    bouquet1.print_bouquet()
    bouquet1.average_withering_time()
    bouquet1.contains_flower("Роза")
    print("Общая стоимость букета: ", bouquet1.total_price())
    print(bouquet1.sort_flowers_by_price())


    bouquet2.print_bouquet()
    bouquet2.average_withering_time()
    bouquet2.contains_flower("Лиллия")
    print("Общая стоимость букета: ", bouquet2.total_price())
    print(bouquet2.sort_flowers_by_price())