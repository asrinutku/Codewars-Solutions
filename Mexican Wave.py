# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:35:50 2021

@author: asrinutku
"""
def wave(str):
    # Code here
    result=[]
    for i in range(len(str)):
        s=list(str)
        if s[i]==" ":
            i=i+1
        else:
            s[i]=s[i].upper()
            result.append(''.join(s))
    return result