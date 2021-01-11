# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:30:22 2021

@author: asrinutku
"""
def expanded_form(num):
    result = []
    i = 1
    for index, digit in enumerate(str(num)[::-1]):    
        if int(digit) != 0:
            if index == 0:
                result.append(str(digit))
            else:
                result.append(str(int(digit)*i))
        i = i*10
    return ' + '.join(result[::-1])