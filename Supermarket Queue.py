# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:35:49 2021

@author: asrinutku
"""
def queue_time(customers, n):
    checkouttills=[0]*n
    for i in customers:
        checkouttills[checkouttills.index(min(checkouttills))]+=i
    return max(checkouttills)