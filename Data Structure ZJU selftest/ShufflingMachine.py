# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:10:56 2020

@author: Deng Jie
"""

spade = ['S' + str(i) for i in range(1, 14, 1)]
heart = ['H' + str(i) for i in range(1, 14, 1)]
club = ['C' + str(i) for i in range(1, 14, 1)]
diam = ['D' + str(i) for i in range(1, 14, 1)]
joker = ['J1', 'J2']
cards = spade + heart + club + diam + joker
result = [None]*len(cards)

K = int(input())
order = list(map(int, input().split()))

for i in range(len(cards)):
    index = i
    for j in range(K):
        index = order[index] - 1
    result[index] = cards[i]
print(' '.join(result))