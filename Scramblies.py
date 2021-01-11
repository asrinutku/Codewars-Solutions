# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:39:06 2021

@author: asrinutku
"""
def scramble(s1,s2):  

    for i in set(s2):
        if s1.count(i) < s2.count(i):
            return False
    return True