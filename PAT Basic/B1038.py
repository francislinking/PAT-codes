N = int(input())
line = [int(x) for x in input().split()]

ldict = {}
for item in line:
    ldict[item] = ldict.get(item,0) + 1

q = [int(x) for x in input().split()]

K = q[0]
result = []
for i in range(1,K+1):
    result.append(str(ldict.get(q[i],0)))

print(' '.join(result))
