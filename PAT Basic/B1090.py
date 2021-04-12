N, M = [int(x) for x in input().split()]

d = {}
for i in range(N):
    a,b = [int(x) for x in input().split()]  
    d[a] = d.get(a,[])
    d[a].append(b)
    d[b] = d.get(b,[])
    d[b].append(a)

# for k,v in d.items():
#     print(k,v)

for i in range(M):
    line = [int(x) for x in input().split()]
    goods = set(line[1::])
    dangerlist = set()
    flag = 0
    for index in goods:
        dangerlist = set(d.get(index,[]))
        if len(dangerlist.intersection(goods)) != 0:
            flag = 1
            break

    if flag == 1:
        print('No')
    else:
        print('Yes')


