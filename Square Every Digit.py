# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:33:18 2021

@author: asrinutku
"""
def square_digits(num):
    if(str(num).isdigit()):       
        z = ''.join(str(int(i)**2) for i in str(num))
        return int(z)
    else:
        return 0