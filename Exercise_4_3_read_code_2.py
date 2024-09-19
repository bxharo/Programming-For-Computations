# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 13:00:36 2024

@author: Brenda
"""

def f(x):
    if x < 2:
        return 0
    else:
        return 2*x
x = 0
for i in range(0, 4, 1):
    x += i
    print(x)
    
for i in range(0, 4, 1):
    x += i*i
print(x)

for i in range(0, 4, 1):
    print('*',f(3*i-1))