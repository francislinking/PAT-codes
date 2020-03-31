'''

'''

firstLine = [int(x) for x in input().split()]

N, L, H = firstLine

records = []

for i in range(N):
    r = [int(x) for x in input().split()]
    s = r[1]+r[2]
    r.append(s)
    records.append(r)

enroll = [x for x in records if x[1]>=L and x[2]>=L]

print(len(enroll))

rank1 = [x for x in enroll if x[1]>=H and x[2]>=H]
rank2 = [x for x in enroll if x[1]>=H>x[2] ]
rank3 = [x for x in enroll if H>x[1]>=x[2] ]
rank4 = [x for x in enroll if x[2]>x[1] and (x[1]<H or x[2]<H)]

rank1.sort(key= lambda x: (x[3],x[1],-x[0]),reverse=True)
rank2.sort(key= lambda x: (x[3],x[1],-x[0]),reverse=True)
rank3.sort(key= lambda x: (x[3],x[1],-x[0]),reverse=True)
rank4.sort(key= lambda x: (x[3],x[1],-x[0]),reverse=True)

result = rank1 + rank2 + rank3 + rank4

for item in result:
    print(' '.join([str(x) for x in item[:-1]]))
