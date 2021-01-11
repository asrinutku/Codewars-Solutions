# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:37:09 2021

@author: asrinutku
"""
def dont_give_me_five(start, end):
    numbers = []

    for i in range(start, end + 1):
        stri = str(i)
        
        if "5" in stri:
            continue
        else:
            numbers.append(i)

    return len(numbers)  # amount of numbers
