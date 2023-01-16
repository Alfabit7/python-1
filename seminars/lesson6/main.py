from functions import *

# list comprehension

lst = [i for i in range(1, 10)]
print(lst)

#  enumerate

lst =  list(enumerate(lst))
print(lst)

# zip

a = [1, 2, 3]
b = ['january', 'february', 'march']

lst1 = list(zip(a, b))
print(lst1)


# lambda

sum = lambda a, b: a + b
print(sum(2, 2))

def summ(a, b, *args):
    x = a + b
    for i in args:
        x += i
    return x

print(summ(2, 3, 4))

# map

lst2 = [i for i in range(1, 10)]
lst2 = list(map(lambda x: x * x, a))
print(lst2)

# filter 


lst3 = [i for i in range(1, 10)]
lst3 = list(filter(lambda x: not x % 2, lst3))
print(lst3)


# sorted

lst4 =[(2, 4, 7), (4, 5, 6), (1, 2, 3)]
res = sorted(lst4, key = lambda x: x[2], reverse=True)
print(res)