# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 20:28:35 2024

@author: Brenda
"""

import numpy as np
import matplotlib.pyplot as plt

def f_(t, a, b):
    return a*t + b

def error_func(a, b):
    E = 0
    for i in range(len(time)):
        E += (f_(time[i],a,b) - data[i])**2
    return E

E = 0
oneMore = True
data = np.array([0.5, 2.0, 1.0, 1.5, 7.5])
time = np.array([0, 1, 2, 3, 4])

while( oneMore == True):
    a = float(input('Enter a value for a: '))
    b = float(input('Enter a value for b: '))
    print(f'The error is {error_func(a, b):.3f}')
    y = f_(time, a, b)
    plt.plot(time, y, time, data, '*')
    plt.xlabel('Time(s)')
    plt.ylabel('y (starts) and straight line f(t)')
    plt.show()
    answer = input('Do you want another fit(y/n)')
    if answer == 'n':
        one_more = False

