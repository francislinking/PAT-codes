# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 23:58:15 2020

@author: Deng Jie
"""

import numpy as np

num, ch =input().split(' ')
num = int(num)

N = np.sqrt((num+1)/2);

N = int(N)

residue = num - (2*np.square(N) - 1)

layers = 2*N - 1

for i in range(layers):
    seq = abs(i - (N - 1)) +1
    rep = 2*seq-1
    str = rep*ch
    zeros = (layers + rep)/2
    zeros = int(zeros)
    #str = str.center(layers,' ')
    str = str.rjust(zeros)
    print(str,end='\n')
    
print(residue)