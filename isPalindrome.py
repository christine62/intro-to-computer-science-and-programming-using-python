#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:13:06 2017

@author: jiahuibi
"""

def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'qwertyuioplkjhgfdsazxcvbnm':
                ans = ans+c
        return ans
    def isPal(s):
        if len(s) <=1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))

print("")
print('Is eve a palindrome?')
print(isPalindrome('eve'))