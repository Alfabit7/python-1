import sys
sys.path.append('/Users/david/Desktop/python/')
from funcs.functions import *

# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

ticket_number = is_natural('Введите номер билетика: ')
while ticket_number < 100000 or ticket_number > 999999:
    print('Номер билетиков шестизначные. Вы ввели что-то другое')
    ticket_number = is_natural('Введите номер билетика: ')

def happy_ticket(number):
    first_half = int(str(ticket_number)[0:3])
    second_half = int(str(ticket_number)[3:6])
    first_half = first_half // 100 + first_half // 10 % 10 + first_half % 10
    second_half = second_half // 100 + first_half // 10 % 10 + second_half % 10
    return first_half == second_half

if happy_ticket(ticket_number):
    print('You are lucky one!')
else:
    print('Sorry. Not this time')
