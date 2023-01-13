#  Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале, игроки ходят поочередно, необходимо вывести карту(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента, каждый из которого обозначает соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик, и проверку на победу( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)

field = list(range(1, 10))
win_combos = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
              (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_field():
    print('-------------')
    for i in range(3):
        print('|', field[0 + i * 3], '|',
              field[1 + i * 3], '|', field[2 + i * 3], '|')
        print('-------------')


def get_input(player_sign):
    while True:
        value = input(f'Куда поставить {player_sign}? ')
        if not (value in '123456789'):
            print('Ошибка. Попробуйте снова')
            continue
        value = int(value)
        if str(field[value - 1]) in 'XO':
            print('Эта клетка уже занята. Попробуйте снова.')
            continue
        field[value - 1] = player_sign
        break


def win_check():
    for each in win_combos:
        if (field[each[0] - 1]) == (field[each[1] - 1]) == (field[each[2] - 1]):
            return field[each[1] - 1]
    else:
        return False


def main_game():
    count = 0
    while True:
        draw_field()
        if not count % 2:
            get_input('X')
        else:
            get_input('O')
        if count > 3:
            winner = win_check()
            if winner:
                draw_field()
                print(f'{winner} выиграл')
                break
        count += 1
        if count > 8:
            draw_field()
            print('Ничья :)')
            break


main_game()
