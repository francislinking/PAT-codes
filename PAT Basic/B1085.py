N = int(input())

ldict = {}
cdict = {}
sdict = {}

for i in range(N):
    ID,score,school = input().split()
    school = school.lower()
    if ID[0] == 'T':
        score = int(score)*1.5
    elif ID[0] == 'A':
        score = int(score)
    elif ID[0] == 'B':
        score = int(score)/1.5
    ldict[school] = ldict.get(school,0) + score
    cdict[school] = cdict.get(school,0) + 1
    sdict[school] = (ldict[school],cdict[school])
    
# print(sdict) 

sdict = sorted(sdict.items(),key = lambda kv:(-kv[1][0],kv[1][1],kv[0]))
rank = 1
temp = 0
print(len(sdict))
for index,item in enumerate(sdict,1):
    name = item[0]
    point = int(item[1][0])
    n = item[1][1]
    if point == temp:
        rank = rank
    else:
        rank = index
    temp = point
    print(rank,name,point,n)