# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:19:56 2020

@author: Deng Jie
"""

cm = int(input())
foot = int(cm/100/0.3048)
inch = int((cm/100/0.3048 - foot)*12)
print(foot,inch)