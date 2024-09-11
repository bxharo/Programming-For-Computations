# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:48:02 2024

@author: Brenda
"""

import numpy as np
import matplotlib.pyplot as plt

v0 = 4.5
g = 9.81

t = np.linspace(0 , 1 , 1000)

y = v0*t -0.5*g*t**2

#Find the index where ball approximately has reached y =0
i=0
while y[i] >= 0:
    i+=1
    
print('The time of the flight in seconds is {:g}'.format(t[i]))

plt.plot(t, y)      #plot all y coordinates vs. all t coordinates
plt.plot(t, 0*t, 'g--')
plt.xlabel('t (s)') # places the text t (s) on x-axis
plt.ylabel('v (m)') # places the text v (m) on y-axis
plt.show()          #displays the figure