# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:14:34 2024

@author: Brenda
"""

import numpy as np

def add_vectors(a, b):
    a = np.array(a)
    b = np.array(b)
    if(len(a)== len(b)):
        c= a+b
        return c
    else:
        return 'It is not posible to add them, they are not the same size '
    
print(add_vectors([2,1,3],[3,8]))