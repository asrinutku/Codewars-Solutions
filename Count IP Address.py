# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:39:05 2021

@author: asrinutku
"""
def ips_between(start, end):

    gap = []
    firstip = start.split(".")
    secondip = end.split(".")
    
    for i in range(len(firstip)):
        gap.append(int(secondip[i])-int(firstip[i]))
    
    return gap[3]+256*gap[2]+(256**2)*gap[1]+(256**3)*gap[0]