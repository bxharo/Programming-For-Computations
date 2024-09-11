# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:41:52 2024

@author: Brenda
"""

import random
import numpy as np
import matplotlib.pyplot as plt

N = 1000        #number of steps
d = 1           #step lenght
x = np.zeros(N + 1)
y = np.zeros(N + 1)

x[0]=0; y[0]=0 # set initial position

step = 0
for i in range(0,N,1):
    r = random.random()
    if(0 <= r < 0.25):
        y[i+1] = y[i] + d
        x[i+1] = x[i]
    elif(0.25 <= r < 0.5):
        x[i+1] = x[i] + d
        y[i+1] = y[i] 
    elif(0.5 <= r < 0.75):
        y[i+1] = y[i] - d
        x[i+1] = x[i]
    else:
        x[i+1] = x[i] - d
        y[i+1] = y[i] 
        
# plot path (mark start and stop with blue o and *, respectively)
plt.plot(x, y, 'r--', x[0], y[0], 'bo', x[-1], y[-1], 'b*')
plt.xlabel('x'); plt.ylabel('y')
plt.show()