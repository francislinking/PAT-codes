import math
R1,P1,R2,P2 = [float(x) for x in input().split()]

R3 = R1 * R2
P3 = P1 + P2

A = R3*math.cos(P3)
B = R3*math.sin(P3)
if -0.01 <= A < 0:
    A = 0
if -0.01 <= B < 0:
    B = 0
print('{:.2f}{:+.2f}i'.format(A,B))