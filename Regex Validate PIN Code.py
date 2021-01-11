# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:27:35 2021

@author: asrinutku
"""
def validate_pin(pin):
    #return true or false
    if (len(pin)==4 or len(pin)==6) and pin.isdigit()==1:
        return(True)
    else:
        return(False)