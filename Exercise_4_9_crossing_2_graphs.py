# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 20:18:46 2024

@author: Brenda
"""
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x

def g(x):
    return x**2


N = int(input('Enter a number: '))
epsilon = float(input('Enter a accepted error: '))
x_values = np.linspace(-4, 4, N)

for i in range(N):
    if abs(f(x_values[i]) - g(x_values[i])) < epsilon:
        print( x_values[i])

