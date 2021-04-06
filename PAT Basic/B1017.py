A,B = input().split()
B = int(B)
L = len(A)
temp = 0
Q = []

div,mod = divmod(int(A[0]),B)
if (div!=0 and L>1 ) or L == 1:
    print(div,end='')

for i in range(1,L):
    div,mod = divmod(int(A[i])+mod*10,B)
    print(div,end = '')

print('',mod)