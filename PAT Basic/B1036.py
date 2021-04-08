N, ch=input().split()

N = int(N)
if N%2 == 0:
    M = int(N/2) - 2
else:
    M = int(N//2) + 1 -2

print(ch*N)
for i in range(M):
    print(ch+' '*(N-2)+ch)
print(ch*N)