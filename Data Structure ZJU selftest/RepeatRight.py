# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:47:22 2020

@author: Deng Jie
"""

N, M = input().split(' ')
string = input().split(' ')
N = int(N)
M = int(M)
result = string[N-M:] + string[:N-M]
print(' '.join(result))