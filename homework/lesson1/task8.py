import sys
sys.path.append('/Users/david/Desktop/python/')
from funcs.functions import *

# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

choco_row = is_natural('Ширина шоколадки: ')
choco_col = is_natural('Высота шоколадки: ')
piece = is_natural('Сколько отламываем: ')

if piece <= choco_col * choco_row:
    if piece == 1 and (piece != choco_col or piece != choco_row):
        print('Не получится отломить')
    else:
        if not piece % choco_col or not piece % choco_row:
            print('Получится отломить')
        else:
            print('Не получится отломить')
else:
    print('Не получится отломить')