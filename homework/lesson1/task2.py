import sys
sys.path.append('/Users/david/Desktop/python/')
from funcs.functions import *
import math
# сумма цифр трехзначного числа

number = math.fabs(Number('Введите число: '))
while number < 100 or number > 999:
    print('Это не трехзначное число')
    number = math.fabs(Number('Введите число: '))
result = number // 100 + number // 10 % 10 + number % 10
print(f'Сумма цифра числа {number} = {result}')