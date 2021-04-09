N = int(input())
a = 0
b = 0
for i in range(N):
    A1,A2,B1,B2 = [int(x) for x in input().split()]
    c = A1 + B1 
    if A2 == c and B2 != c:
        b = b + 1
    if A2 != c and B2 == c:
        a = a + 1

print(a,b)