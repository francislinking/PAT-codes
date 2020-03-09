# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:33:16 2020

@author: Deng Jie
"""

def eratosthenes(n):
    IsPrime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False
    return [x for x in range(2, n + 1) if IsPrime[x]]

n=int(input())
result = eratosthenes(n)
#print(result)
count = 0;
for i in range(len(result) - 1):
    if result[i+1]-result[i]== 2:
        count +=1;
print(count)