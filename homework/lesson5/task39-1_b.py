# Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил

# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

# ЧЕЛОВЕК ПРОТИВ УМНОГО БОТА. Если он ходит первым, то выиграть невозможно
from functions import *
from random import randint

player_1 = input('Первый игрок, представьтесь: ')
player_2 = 'Smart bot'
candy_value = is_natural('Введите количество конфет на столе: ')


def candy_amt(player_name):
    candys = is_natural(f'{player_name}, введите количество конфет, которое вы хотите взять (от 1 до 28): ')
    while candys > 28:
        candys = is_natural(f'{player_name}, нужно ввести число от 1 до 28. Попробуйте снова: ')
    return candys

def round(player, amt, value):
    print(f'{player} взял {amt} конфет. На столе осталось {value} конфет.')
    

def main_game(candy_value):
    
    # flag = randint(0, 2)
    flag = 0
    if flag:
        print(f'Первым ходит {player_1}')
    else:
        print(f'Первым ходит {player_2}')
    
    while  candy_value > 28:
        if flag:
            number = candy_amt(player_1)
            candy_value -= number
            flag = 0
            round(player_1, number, candy_value)
        else:
            if candy_value % 29:
                number = candy_value % 29
            else:
                number = randint(1, 29)
            candy_value -= number
            flag = 1
            round(player_2, number, candy_value)
    if flag:
        print(f'{player_1}, поздравляю, вы выиграли!')
    else:
        print(f'{player_2}, поздравляю, вы выиграли!')    


main_game(candy_value)

  


            





