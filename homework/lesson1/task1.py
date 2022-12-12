import sys
sys.path.append('/Users/david/Desktop/python/')
from funcs.functions import *

# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

days = ('Empty', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
day = Number("Введите номер дня недели (от 1 до 7): ")
while day > 7 or day > 1:
    print('Такого дня недели нет. Нужно ввести цифру от 1 до 7.')
    day = Number("Введите номер дня недели (от 1 до 7): ")
if day == 6 or day == 7:
    print(f'Да, {days[day]} - выходной')
else:
    print(f'Нет, {days[day]} - не выходной')