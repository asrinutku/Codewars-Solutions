# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:29:15 2021

@author: asrinutku
"""
def alphabet_position(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text = list(text)
    result = []
    for x in text:
        if x.isalpha():
            result.append(str(alphabet.index(x.lower())+1))
    return ' '.join(filter(None, result))


text = "The sunset sets at twelve o clock"
alphabet_position(text)