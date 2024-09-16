# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:59:30 2024

@author: Brenda
"""
import random

N = int(input('Write a positive integer: ')) 
i = 0
M= 0

while i < N:
    rand_int = random.randint(1, 6)
    print('Draw number {:d} gave:  {:d}'.format(i +1,rand_int))
    if(rand_int == 6):
        M +=1
    i += 1
    
print(M/N)