N, M = [int(x) for x in input().split()]


edge = []
weight = []
for i in range(M):
    v1, v2, w = map(int,input().split())
    edge.append((v1,v2))
    weight.append(w)

VertexList = [-1 for i in range(N)]
visited = 0
l_msn = 0

def find(item):
    if VertexList[item]<0:
        return item
    else:
        return find(VertexList[item])

def union(r1,r2):
    if VertexList[r1]<VertexList[r2]:
        VertexList[r1]+=VertexList[r2]
        VertexList[r2] = r1
    else:
        VertexList[r2]+=VertexList[r1]
        VertexList[r1] = r2



#Kruskal
while(visited <N and weight!=[]):
    index = weight.index(min(weight))
    min_weight = weight.pop(index)
    this_edge = edge.pop(index)
    r1 = find(this_edge[0]-1)
    r2 = find(this_edge[1]-1)
    if r1 != r2:
        union(r1,r2)
        l_msn +=min_weight
        if visited == 0:
            visited +=2
        else:
            visited +=1

if visited == N:
    print(l_msn)
else:
    print(-1)
