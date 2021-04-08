N = int(input())
line = [int(x) for x in input().split()]

ldict = {}

for i in range(1,N+1):
    d = abs(line[i-1] - i)
    ldict[d] = ldict.get(d,0) + 1

ldict = sorted(ldict.items(), key = lambda kv : kv[0],reverse = True)

for item in ldict:
    if item[1] != 1:
        print(item[0],item[1])