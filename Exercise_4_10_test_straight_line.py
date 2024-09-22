# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 17:26:48 2024

@author: Brenda
"""

import numpy as np

def function_(x):
    return 4*x + 1

slope = 4
a = 0
b = 1000

n = 100

for i in np.linspace(a, b, n):
    fraction = (function_(i) - function_(2))/(i - 2)
    print(f"{i:.3f} and {abs(fraction - slope):.3f}")
 
   