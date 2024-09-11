# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:44:45 2024

@author: Brenda
"""
from math import pi

r = 10.6
a = 1.3
b = 0

a_rectangle = a*b
a_circle = pi*r**2


while a_rectangle < a_circle:
    b +=1
    a_rectangle = a*b
    
b -= 1    
print('The largest posible integer b is {:d}'.format(b))