# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 13:07:01 2024

@author: Brenda
"""
from numpy import pi

r = float(input('Ingresa el radio: '))

def circunference(r):
    return 2 * pi * r

def area(r):
    return pi * r**2

C = circunference(r)
A = area(r)

print('The circunference for r is {:.3f}'.format(C))
print('The area for r is {:.3f}'.format(A))