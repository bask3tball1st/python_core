from collections import Counter

numbers = [1, 5, 2, 9, 2, 9, 1]
count_of_numbers = Counter(numbers)
for key, value in count_of_numbers.items():
    if value != 1:
        continue
    else:
        print(key)