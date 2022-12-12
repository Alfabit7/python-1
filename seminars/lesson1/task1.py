from functions import *
import math



# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

day_distance = is_natural('Сколько км машина проезжает за день: ')

distance = is_natural('Сколько км ехать: ')

days = math.ceil(distance / day_distance)
print(f'Дней нужно, чтобы проехать {distance} км: {days}')
