# # Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

from functions import *

a1 = is_natural('Введите 1-й член последовательности: ')
d = is_natural('Введите шаг последовательности: ')
n = is_natural('Введите количество чисел последовательности: ')

print([a1 + (n - 1) * d for n in range(1, n + 1)])
