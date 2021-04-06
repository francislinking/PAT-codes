M,N,A,B,R = input().split()
M = int(M)
N = int(N)
A = A.zfill(3)
B = B.zfill(3)
R = R.zfill(3)

for i in range(M):
    line = input().split()
    for j in range(N):
        line[j] = str(line[j]).zfill(3)
        if A<=line[j]<=B:
            line[j] = R
    print(' '.join(line))