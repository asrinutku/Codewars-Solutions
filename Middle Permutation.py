# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:39:05 2021

@author: asrinutku
"""
def middle_permutation(string):
    if string:
        if len(string) % 2 == 1:
            string = ''.join(sorted(string))
            first = string[len(string) // 2]
            string = ''.join([i for i in string if i != first])
            return first + middle_permutation(string)
        else:
            string = ''.join(sorted(string, reverse=True))
            first = string[len(string) // 2]
            string = ''.join([i for i in string if i != first])           
            return first + string
    else:
        return ''