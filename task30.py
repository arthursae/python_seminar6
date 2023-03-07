# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

# pytest -v tests\test_30.py

def arithmetic_progression(first: int,
                           diff: int,
                           quantity: int) -> list[int]:
    return [i for i in range(first, quantity * diff + 1, diff)]


first = int(input('Введите первый эдемент: '))
diff = int(input('Введите разность: '))
quantity = int(input('Введите количество элементов: '))

print(arithmetic_progression(first, diff, quantity))
