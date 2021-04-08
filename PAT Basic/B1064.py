N = int(input())
line = [str(x) for x in input().split()]

ldict = {}

for item in line:
    s = 0
    for c in item:
        s = s + int(c)

    ldict[s] = ldict.get(s,0) + 1

ldict = sorted(ldict.keys())

print(len(ldict))
print(' '.join(list(map(str,ldict))))  