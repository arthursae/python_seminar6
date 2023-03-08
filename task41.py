# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Элементы массива вводятся на одной строке через пробел. Массив состоит из целых чисел.
# Список не циклический
# [1, 2, 1, 3, 4, 3] -> 2 (2, 4)

from random import randint

numbers = [randint(1, 5) for i in range(10)]
counter = 0
for i in range(1, len(numbers) - 1):
    print(numbers[i - 1], numbers[i], numbers[i + 1])
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        counter += 1
print(numbers, '->', counter)
