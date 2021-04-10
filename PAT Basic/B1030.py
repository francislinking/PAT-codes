N, p =[int(x) for x in input().split()]
nlist = [int(x) for x in input().split()]
nlist.sort()

result = 0
i = 0
j = i + result

while(i < N):
    while(j < N):
        m = nlist[i]
        M = nlist[j]
        if m * p >= M:
            length = j - i + 1
            result = length if length > result else result
        else:
            break
        j = j + 1
    i = i + 1
    j = i + result

print(result)