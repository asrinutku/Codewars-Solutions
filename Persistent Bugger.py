# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:35:25 2021

@author: asrinutku
"""
def persistence(n):
    number = str(n)
    count = 0
    if(len(number) == 1):
        return len(number)-1
    else:
        while(len(number)>1):
            newnumber = 1
            
            for i in number:
                newnumber = newnumber * int(i)
  
            number =str(newnumber)
            count += 1
        return count
        