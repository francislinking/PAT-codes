N = int(input())

cdict = {}

for i in range(N):
    sid,score = [int(x) for x in input().split()]
    cdict[sid] = cdict.get(sid,0) + score

cdict = sorted(cdict.items(), key = lambda kv:kv[1],reverse=True)

print(cdict[0][0],cdict[0][1])