# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:31:40 2021

@author: asrinutku
"""
def narcissistic( value ):
    length =len(str(value))
    sum =0
    for i in str(value):
        sum += int(i)**length
    if sum == value:
        return True
    else:
        return False