# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 19:01:39 2024

@author: Brenda
"""

import numpy as np
import matplotlib.pyplot as plt

v0 = 5
g = 9.81

t = np.linspace(0 , 1 , 11)

y = v0*t -0.5*g*t**2

plt.plot(t,y,'b*',) # k - black, b - blue, r - red, g - green, ...
plt.xlabel('time')
plt.ylabel('velocity')
plt.legend(['v0*t -  0.5*g*t**2'])
plt.grid('on')
plt.title('This is a great title')
plt.axis([0, 1.2, -0.2, 1.5])
plt.show()

