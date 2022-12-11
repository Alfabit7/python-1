import sys
sys.path.append('/Users/david/Desktop/python/')

from funcs.functions import *

def fib(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fib(x-2) + fib(x-1)


def fact(x):
    if x == 0:
        return 1
    else:
        x = x * fact(x - 1)
        return x
from math import pi

print(pi)