# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:35:42 2024

@author: Brenda
"""

b = int(input('Enter the height of a rectangle: '))
c = int(input('Enter the width of a rectangle: '))
A = 0

def area(b, c):
    A = b*c
    return A

print('The result area of the rectangle is {:d}'.format(area(b,c)))