#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 12:03:32 2017

@author: jiahuibi
"""

cube=27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3-cube)>=epsilon and guess <=cube:
    guess += increment
    num_guesses += 1
print("num_guesses =", num_guesses)
if abs(guess**3-cube)>=epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess,'is close to the cube root of', cube)
    '''
    https://docs.python.org/3/tutorial/floatingpoint.html
    '''
