# 43)Имеется список id сотрудников из 10 элементов, каждый id - случайное число от 1 до 100 (сделать с помощью list_comprehension)
# Имеется список имен сотрудников из 10 элементов (вручную)

# Сопоставьте каждому имени сотрудника его id по порядку, и выведите получившийся список кортежей.

# Отсортировать список по возрастанию id.

# Выведете имена сотрудников, получившие нечетное id.

# Решить с помощью zip,filter,lambda

from random import randint

ids = [randint(1, 100) for i in range(10)]

employee = ['Ivan', 'Petr', 'Max', 'Oleg', 'Tom', 'Pavel', 'Kolya', 'Mike', 'Lena', 'Olya']

employee_list = list(zip(ids, employee))
print(f'Список сотрудников и их id: {employee_list}')

employee_list = list(sorted(employee_list, key = lambda x: x[0]))
print(f'Отсортированный по id список сотрудников: {employee_list}')

employee_list = list(filter(lambda x: x[0] % 2, employee_list))
employee_list = [val for indx, val in employee_list]
print(f'Сотрудники с нечетным id: {employee_list}')