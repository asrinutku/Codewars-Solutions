# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 19:19:32 2021

@author: asrinutku
"""
def score(dice):
    one = dice.count(1)
    two = dice.count(2)
    three = dice.count(3)
    four = dice.count(4)
    five = dice.count(5)
    six = dice.count(6)
    
    score = 0
    
    if one < 3: score += 100 * one
        
    elif one >= 3: 
        score += 1000
        one -= 3
        if (one==1):
            score += 100
        if (one==2):
            score += 200
        

    if five < 3:
        score+= 50 * five
    
    elif five >= 3: 
        score += 500
        five -= 3
        if (five==1):
            score += 50
        if (five==2):
            score += 100
    
        
    if two >= 3: score += 200
    elif three >= 3 : score += 300
    elif four >= 3 : score += 400
    elif six >= 3 : score += 600
        
    return score
        