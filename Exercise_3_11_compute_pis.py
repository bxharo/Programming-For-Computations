# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:51:52 2024

@author: Brenda
"""

from numpy import pi, zeros, sqrt
import matplotlib.pyplot as plt


N = int(input('Give a number: '))
pi_leibniz = 0
Leibniz_error = zeros(N)
pi_euler = 0
Euler_error = zeros(N)

for i in range(0,N):
     pi_leibniz += 1/((4*i + 1)*(4*i + 3))
     Leibniz_error[i] = pi - 8*pi_leibniz
     
for i in range(1,N+1):
    pi_euler += 1/(i**2)
    Euler_error[i-1] = pi - sqrt(6*pi_euler)
     
pi_leibniz *= 8
pi_euler *= 6
pi_euler =pi_euler**(1/2)

print('The number is {:.6f}, {:.6f}'.format(pi_leibniz, pi_euler))

plt.plot(range(N), Leibniz_error, 'b-',\
         range(N), Euler_error, 'r-')
plt.xlabel('No of terms')
plt.ylabel('Error with Leibniz (blue) and Euler (red)')
plt.show()