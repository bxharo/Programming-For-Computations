# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:24:28 2024

@author: Brenda
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.zeros(4, float)
y = np.zeros(4, float)
z = np.zeros(4, int)


x = np.array([1.60, 1.85, 1.75, 1.80])
y = np.array([0.50, 0.70, 1.90, 1.75])
z = np.linspace(1, 4, 4,dtype=int)

plt.plot(z, x, 'r*', z, y , 'b*')
plt.axis([0,5,0,2])
plt.show()





