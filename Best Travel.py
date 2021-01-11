# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:39:05 2021

@author: asrinutku
"""
import itertools

def choose_best_sum(t, k, ls):
    combinations = itertools.combinations(ls, k)
    bestsum = 0
    if ( k == 0 or t == 0 or ls == 0):
        return None
    for grups in combinations:
        sumofgrup = sum(grups)
        if sumofgrup <= t and sumofgrup > bestsum:
            bestsum = sumofgrup
    if (bestsum == 0):
        return None
    return bestsum