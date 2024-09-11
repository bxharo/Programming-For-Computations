# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:21:58 2024

@author: Brenda
"""

import numpy as np
import matplotlib.pyplot as plt

v0 = 5
g = 9.81

t = np.linspace(0 , 1 , 1000)

y = v0*t -0.5*g*t**2

largest_height = y[0]

for i in range(1, len(y), 1):
    if(y[i] > largest_height ):
        largest_height = y[i]
        
print('The largest height achieved was {:g} m'.format(largest_height))

plt.plot(t, y)      #plot all y coordinates vs. all t coordinates
plt.xlabel('t (s)') # places the text t (s) on x-axis
plt.ylabel('v (m)') # places the text v (m) on y-axis
plt.show()          #displays the figure