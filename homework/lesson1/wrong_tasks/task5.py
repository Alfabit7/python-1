import sys
from math import sqrt
sys.path.append('/Users/david/Desktop/python/')
from funcs.functions import *

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def distance_2d(point_x1, point_y1, point_x2, point_y2):
    result = sqrt((point_x2 - point_x1) ** 2 + (point_y2 - point_y1) ** 2)
    return result

point_x1 = Number('Введите точку x1')
point_x2 = Number('Введите точку x2')
point_y1 = Number('Введите точку y1')
point_y2 = Number('Введите точку y2')

distance = (distance_2d(point_x1, point_y1, point_x2, point_y2))
distance = round(distance, 3)

print(f'Рассточние между точками A({point_x1}, {point_y1}) и B({point_x2}, {point_y2}) = {distance}')

