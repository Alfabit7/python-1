import sys
sys.path.append('/Users/david/Desktop/python/')
from funcs.functions import *

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = Number('Введите номер четверти')
while quarter < 1 or quarter > 4:
    print('Нужно ввести цифру от 1 до 4')
    quarter = Number('Введите номер четверти')

if quarter == 1:
    print(f'Диапазон точек в {quarter} четверти: x(0, +∞), y(0, +∞)')
elif quarter == 2:
    print(f'Диапазон точек в {quarter} четверти: x(0, -∞), y(0, +∞)')
elif quarter == 3:
    print(f'Диапазон точек в {quarter} четверти: x(0, -∞), y(0, -∞)')
else:
    print(f'Диапазон точек в {quarter} четверти: x(0, +∞), y(0, -∞)')