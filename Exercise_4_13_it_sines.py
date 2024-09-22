# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:55:35 2024

@author: Brenda
"""
import numpy as np
import matplotlib.pyplot as plt

def sinesum(t, b):
    """
    Parameters
    ----------
    t : TYPE
        DESCRIPTION.
    b : TYPE
        DESCRIPTION.

    Returns sum of sines representing a signal of a t time
    -------
    """
    
    SN_t = np.zeros(len(t))
    
    for j in range(0, len(t), 1):
        for i in range(1, len(t) + 1 ,1):
            SN_t[j] += b[i-1]*np.sin(i*t[j])
    return SN_t
     
        
def test_sinesum():
    """
    

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    t = np.array([-np.pi/2, -np.pi/4 ])     #array of time coordinates
    b = np.array([4, -3])                   #array of bn coeficients
    
    return sinesum(t, b)

def f(t):
    return (1/np.pi)*t

def plot_compare(f, N, M):
    plt.plot(range(len(test_sinesum())), result, marker='o', label='Sine Sum')
    plt.xlabel('Uniformily distributed t coordinates used to plot f and SN')
    plt.ylabel('Sn(t) and f(t)')
    plt.title('Comparing Sn(t) and f(t)')
    plt.legend()
    plt.grid(True)
    plt.show()

result = test_sinesum()
print(result)
plot_compare(1, 2, 2)