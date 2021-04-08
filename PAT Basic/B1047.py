N = int(input())

ldict = {}
for i in range(N):
    gid_uid, point = input().split()
    gid,uid = gid_uid.split('-')
    ldict[gid] = ldict.get(gid,0) + int(point)

maxvalue = max(ldict.items(), key = lambda kv:kv[1])

print(maxvalue[0],maxvalue[1])