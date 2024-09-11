# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:15:36 2024

@author: Brenda
"""

T = float(input('What\'s the temperature is the water'))

if T > 24:
    print('Great, Jump in!')
elif 20 < T < 24:
    print('Not bad. Put your toe in first')
else:
    print('Do not swim. Too cold')
        