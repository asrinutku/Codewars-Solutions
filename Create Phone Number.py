# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:34:48 2021

@author: asrinutku
"""
def create_phone_number(n):


    n.insert(0,"(")
    n.insert(4,")")
    
    n.insert(5," ")
    n.insert(9,"-")
    
    return "".join(str(x) for x in n )