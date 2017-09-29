#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:31:51 2017

@author: jiahuibi
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '':
        return False

    if len(aStr) == 1:
        return char == aStr 
    mid=int(len(aStr)/2)
    midchar = aStr[mid]
    if char == midchar:
        return True
    elif char<midchar:
        return isIn(char,aStr[:mid])
    else:
        return isIn(char,aStr[mid:])
        
#Test Code
isIn('s', 'bfhopy')

isIn('c', 'bcddfhqwyz')