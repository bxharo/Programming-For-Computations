# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 19:22:57 2024

@author: Brenda
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2,2,100)
f_values = t**2
g_values = np.exp(t)

plt.plot(t,f_values,'r', t, g_values, 'k--')

plt.xlabel('range from -2 to 2')
plt.ylabel('y and y1')
plt.legend(['t**2','e**t'])
plt.grid('on')
plt.title('Plotting two functions (t**2 and e**t)')
plt.axis([-3,3,-1,10])
plt.show()