school = {}
symbol_list = ("a", "б", "в", "г", "д", "е", "к", "л", "м", "н")
count = 20

for class_number in range(10):
    school[str(class_number + 1) + symbol_list[class_number]] = class_number + count

print(school)
