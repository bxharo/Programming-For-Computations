# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:10:47 2024

@author: Brenda
"""

import numpy as np
N = 5
h = np.zeros(N, dtype = float)
h[0] = 1.60; h[1] = 1.85; h[2] = 1.75; h[3] = 1.80; h[4] = 0.50

sum_ = 0

for i in [0, 1, 2, 3, 4]:
    sum_ += h[i]

average = sum_/N
print('The average of the five family members is {:.3f}'.format(average))    

