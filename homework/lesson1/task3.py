import sys
sys.path.append('/Users/david/Desktop/python/')
from funcs.functions import *

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .

point_x = Number('Введите x')
while point_x == 0:
    point_x = Number('Введите число больше 0')
point_y = Number('Введите y')
while point_y == 0:
    point_y = Number('Введите число больше 0')

if point_x > 0 and point_y > 0:
    print(f'Точка ({point_x}, {point_y}) находится в I четверти')
elif point_x < 0 and point_y > 0:
    print(f'Точка ({point_x}, {point_y}) находится в II четверти')
elif point_x < 0 and point_y < 0:
    print(f'Точка ({point_x}, {point_y}) находится в III четверти')
else:
    print(f'Точка ({point_x}, {point_y}) находится в IV четверти')
