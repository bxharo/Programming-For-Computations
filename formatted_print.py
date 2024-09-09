# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 22:21:32 2024

@author: Brenda
"""
v1 = 2
v2 = 4

print('v1 is {a} \nv2 is {b}'.format(a=v1,b=v2))
print(f'v1 is {v1} \nv2 is {v2}') #another way

r = 12.89643 # real number
i = 42 # integer
s = 'some message' # string (equivalent: s = "some message")

print('real number:{: .3f} \ninteger:{:d}  \nstring:{:s}'.format(r,i,s))
print('real number:{:9.3e} \ninteger:{:5d}  \nstring:{:s}'.format(r,i,s))

print("""This is a long string that will run over several lines
         if we just manage to fill in
         enough words.""")