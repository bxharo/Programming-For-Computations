# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:26:52 2024

@author: Brenda
"""

import numpy as np

# Simplified values for y
y = np.array([1, 3, 2, 4])  # Integers with a clear maximum

# Initialize largest_height
largest_height = y[0]

# Loop to find the largest value and print progress
for i in range(1, len(y), 1):
    if y[i] > largest_height:
        largest_height = y[i]
    print(f'Iteration {i}: largest_height = {largest_height}')

# Final result
print('The largest height achieved was {:g}'.format(largest_height))