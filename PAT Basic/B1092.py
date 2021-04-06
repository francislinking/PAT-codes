N,M = [int(x) for x in input().split()]

s = [0]*N

for i in range(M):
    line = [int(x) for x in input().split()]
    for j in range(N):
        s[j] = s[j] + line[j]

max_value = max(s)
print(max_value)
max_index = [str(index) for (index,item) in enumerate(s,1) if item == max_value]
print(' '.join(max_index))