# -*- coding: utf-8 -*-
from __future__ import division
import re


# import matplotlib.pyplot as plt

# for i in [1, 2, 3, 4, 5]:
#     print i
#     for j in [1, 2, 3, 4, 5]:
#         print j
#         print i + j
#     print(i)
# print("Done Looping")

# my_regex = re.compile("[0-9]]", re.I)


def multiplie(x):
    """Aqui é onde vc coloca"""
    return x * 2


def apply_to_one(f):
    return f(1)


my_double = multiplie
x = apply_to_one(my_double)

print(my_double)
print(x)

y = apply_to_one(lambda x: x + 4)
print(y)


def myPrint(message="Hello"):
    print(message)


myPrint()
myPrint('TESTE')
myPrint(message='NOIS')


try:
    print 0 / 0
except ZeroDivisionError:
    print "Cannot divide by zero"