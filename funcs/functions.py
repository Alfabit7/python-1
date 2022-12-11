from random import randint

def Number(text):
    number = input(f'{text}: ')
    while(not number.isdigit()):
        number = input('ОШИБКА. Попробуйте снова: ')
    return int(number)

        
