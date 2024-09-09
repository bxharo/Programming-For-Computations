# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:09:22 2024

@author: Brenda
"""

import random

a = 1; b = 6
random.seed(10)

r1 = random.randint(a, b)   # first die
r2 = random.randint(a, b)   #second die

print('The dice gave: {:d} and {:d}'.format(r1, r2))