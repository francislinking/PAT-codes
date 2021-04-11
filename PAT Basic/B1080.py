P, M, N = [int(x) for x in input().split()]
d = {}
for i in range(P):
    sid,pnt = input().split()
    pnt = int(pnt)
    d[sid] = d.get(sid,(-1,-1,-1,0))
    d[sid] = (pnt,d[sid][1],d[sid][2],-1)

for i in range(M):
    sid,pnt = input().split()
    pnt = int(pnt)
    d[sid] = d.get(sid,(-1,-1,-1,0))
    d[sid] = (d[sid][0],pnt,d[sid][2],-1)

for i in range(N):
    sid,pnt = input().split()
    pnt = int(pnt)
    d[sid] = d.get(sid,(-1,-1,-1,0))
    d[sid] = (d[sid][0],d[sid][1],pnt,-1)

result = []

for k in d.keys():
    G = 0
    if d[k][0] >= 200:
        if d[k][1] > d[k][2]:
            G = round(0.4*d[k][1] + 0.6*d[k][2])
        else:
            G = d[k][2]

        if G >= 60:
            d[k] = (d[k][0],d[k][1],d[k][2],G)
            # print(k,d[k])
            result.append((k,d[k]))

result.sort(key = lambda x:(-x[1][3],x[0]))

for item in result:
    print(item[0],' '.join((str(x) for x in item[1])))

