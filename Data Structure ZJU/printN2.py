# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:48:24 2020

@author: Deng Jie
"""

def printN( N ):
    if N == 1:
        print(1)
    else:
        printN( N-1 )
        print(N)
        
n = eval(input())

printN(n) 