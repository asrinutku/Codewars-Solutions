# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:29:49 2021

@author: asrinutku
"""
def toJadenCase(string):
        return " ".join(word[0].upper() + word[1:] for word in string.split())