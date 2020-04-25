# https://blog.csdn.net/Invokar/article/details/80308178
N = int(input())
line1 = [ int (x) for x in input().split() ]
table = [0]*N

# generate pointer array
for index in range(N):
    table[line1[index]] = index

# def swap(A,i,j):
#     A[i],A[j] = A[j],A[i]

i = 0
if line1[0] == 0:
    K = 2
else:
    K = 0 
count = 0
# traverse
for i in range(N):
    if(line1[i]!=i):
        K+=1
        hold = i
        curr = hold
        ptr = table[i]
        # loop
        count+=1
        while (ptr!=hold):
            line1[curr],line1[ptr] = line1[ptr],line1[curr]
            table[curr] = curr
            curr = ptr
            ptr = table[curr]
            count+=1

S = N-count
if N == 1:
    print(0)
else:
    print(N-S+K-2)