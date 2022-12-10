def Number():
    number = input('Введите число: ')
    while(not number.isdigit()):
        number = input('Вы ввели не число. Попробуйте снова: ')
    return int(number)


