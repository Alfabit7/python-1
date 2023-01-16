# Задача 31: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

from random import randint
from functions import *

size = is_natural('Введите длину списка: ')
numbers = [randint(-10, 10) for i in range(size)]
print(f'Ваш список: {numbers}')

mini = Number('Введите нижнюю границу диапазона: ')
maxi = Number('Введите верхнюю границу диапазона: ')

result = [i for i in range(len(numbers)) if mini < numbers[i] < maxi]
print(f'Индексы элементов в диапазоне от {mini} до {maxi}: {result}')


