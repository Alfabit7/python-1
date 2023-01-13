# 36. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.

# *Пример:*

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

list = [2, 5, 2, 3, 4, 6, 1, 7]

def inc_list(list):
    result= [list[0]]
    count = 0
    for i in range(1, len(list)):
        if list[i] > result[count]:
            result.append(list[i])
            count += 1
    return result

print(inc_list(list))

