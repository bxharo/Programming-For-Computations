# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:36:02 2024

@author: Brenda
"""

import random
game = True
sum_part1 = 0
upper_limit = 21

while(game):
    participant_1 =  str(input('Do you want another draw?'))
    if(participant_1 == 'yes'):
        draw = random.randint(1,10)
        sum_part1 += draw
        print('You got {:d} and have a total of {:d}'.format(draw,sum_part1))
        if(sum_part1 > upper_limit):
            print('You lose!')
            game = False
    else:
        print('You got {:d}'.format(sum_part1))
        game = False

print('Game Over')
        