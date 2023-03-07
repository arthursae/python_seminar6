# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

# pytest -v tests\test_32.py

from random import randint

# min_num = int(input('Введите минимальное число: '))
# max_num = int(input('Введите максимальное число: '))
# num_lst = [randint(-10, 10) for i in range(20)]
min_num = 5
max_num = 15
num_lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]


def is_in_mass(num_lst: list[int],
               min_num: int,
               max_num: int) -> list[int]:
    """Возвращает список индексов элементов списка, которые
    находятся в диапазоне [min_num,max_num) """
    indecies = list()
    for index, number in enumerate(num_lst):
        if min_num <= number <= max_num:
            indecies.append(index)
    return indecies


print(is_in_mass(num_lst, min_num, max_num))
