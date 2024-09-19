# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:42:34 2024

@author: Brenda
"""


def average(a):
    """
    Computes the average of all integers i = 1, . . . ,a
    """
    if a > 1:
        sum_ = 0
        for i in range(1, a+1, 1):
            sum_ += i
        return 'The average is {:.3f}, {sum_/(a))}'
    return 'That number is not larger than 1'

N = int(input('Enter a number, larger than 1: '))

print(average(N))
