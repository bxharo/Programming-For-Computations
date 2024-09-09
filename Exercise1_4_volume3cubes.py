# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 18:34:50 2024

@author: Brenda
"""
import numpy as np
import matplotlib.pyplot as plt

#In a program, use the linspace function to compute and print three values of L,
#equally spaced on the interval [1, 3].

x = (np.linspace(1,3,3)).astype(int)

#Modify the program in a), so that it prints out the result V of V = L**3 when L is
#an array with three elements as computed by linspace. Compare the resulting
#volumes with your hand calculations.

y = x**3

print(y)

#Make a plot of V versus L.
plt.plot(x,y)
plt.xlabel("Lenght")
plt.ylabel("Volume")
plt.title("Volume of a cube")

plt.show