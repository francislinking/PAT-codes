# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:19:14 2020

@author: Deng Jie
"""

N = int(input())
doubleN = N*2

str_N = str(N)
str_doubleN = str(doubleN)

Set_N = set(str_N)
Set_doubleN = set(str_doubleN)

if Set_N == Set_doubleN:
    print("Yes")
else:
    print("No")
    
print(doubleN)