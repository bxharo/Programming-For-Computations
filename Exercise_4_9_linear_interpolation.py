# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:43:08 2024

@author: Brenda
"""
import numpy as np

y = np.array([])

def interpolate(y, t):
    """
    """
    i = int(t)
    # y(t) = y_i + ((y_i+1 -y_i)/(t_1+1 - t_1))*(t - i)
    return y[i] +((y[i+1] - y[i])/delta_t)*(t-i)

def find_y():
    """Repeatedly finds y at t by interpolation"""
    print(f"For time t on the interval [0,{N:2d}]...")
    t= float(input('Give your desired t > 0: '))
    while t >= 0:
        print(f"y(t) = {interpolate(y,t):g}")
        t = float(input('Give new time t (to stop, enter t < 0): '))
        
N = 4
delta_t = 1.0    # Time difference between measurements
t = 0

y = np.zeros(5)
y[0] = 4.4; y[1] = 2.0; y[2] = 11.0;
y[3] = 21.5; y[4] = 7.5

find_y()