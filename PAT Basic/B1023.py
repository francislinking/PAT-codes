line = [int(x) for x in input().split()]
nlist = []
nZero = line[0]
for i in range(10):
    if line[i]:
        nlist.extend([i]*line[i])

first = nlist.pop(nZero)
nlist.insert(0,first)
nlist = list(map(str,nlist))
print(''.join(nlist))