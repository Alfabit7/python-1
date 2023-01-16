# 41)Напишите программу на Python для поиска пересечения двух заданных массивов с помощью Lambda, filter.
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]

list1 = [1, 2, 3, 5, 7, 8, 9, 10]
list2 = [1, 2, 4, 8, 9]

result = list(filter(lambda x: x in list2, list1))
print(result)
