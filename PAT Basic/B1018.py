N = int(input())

# sort, min char firsr
cjb_list = ['B','C','J']
# counts of win for C,J,B
A = [0,0,0]
B = [0,0,0]
aw = 0
bw = 0

for i in range(N):
    a, b = input().split()
    if a == 'C' and b == 'J': # former win  later
        A[1] = A[1] + 1
        aw = aw + 1
    elif a == 'C' and b == 'B':
        B[0] = B[0] + 1
        bw = bw + 1
    elif a == 'J' and b == 'C':
        B[1] = B[1] + 1
        bw = bw + 1
    elif a == 'J' and b == 'B':
        A[2] = A[2] + 1
        aw = aw + 1
    elif a == 'B' and b == 'C':
        A[0] = A[0] + 1
        aw = aw + 1
    elif a == 'B' and b == 'J':
        B[2] = B[2] + 1
        bw = bw + 1

print(aw,N-aw-bw,bw)
print(bw,N-aw-bw,aw)

am = A.index(max(A))
bm = B.index(max(B))

print(cjb_list[am],cjb_list[bm])
