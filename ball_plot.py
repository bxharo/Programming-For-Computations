# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 19:15:28 2024

@author: Brenda
"""
import numpy as np
import matplotlib.pyplot as plt

v0 = 5
g = 9.81

t = np.linspace(0 , 1 , 1001)

y = v0*t -0.5*g*t**2

plt.plot(t, y)      #plot all y coordinates vs. all t coordinates
plt.xlabel('t (s)') # places the text t (s) on x-axis
plt.ylabel('v (m)') # places the text v (m) on y-axis
plt.show()          #displays the figure