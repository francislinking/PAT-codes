def calc(n):
    return int(n/2) + int(n/3) + int(n/5)

N = int(input())
nlist = []
for n in range(1,N+1):
    nlist.append(calc(n))

print(len(set(nlist)))
