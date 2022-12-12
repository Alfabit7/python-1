import sys
sys.path.append('/Users/david/Desktop/python/')
from funcs.functions import *

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

x = Number('Введите x')
y = Number('Введите y')
z = Number('Введите z')

result = not(x or y or z) == (not(x) and not(y) and not(z))
print(result)