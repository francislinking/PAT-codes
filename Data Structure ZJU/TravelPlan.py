'''
Dijkstra算法，有权图单源最短路
城市间距离（边的权重）存入MCity矩阵
城市间花费（边的次权重）存入MCost矩阵
城市连接关系存入邻接表LCity
调用Dijkstra，注意点距离相同时选花费更少的
'''

firstLine = [int(x) for x in input().split()]
#city, road, source, destination
N = firstLine[0]
M = firstLine[1]
S = firstLine[2]
D = firstLine[3]

MCity = [ [ 0 for i in range(N) ]  for j in range(N)]
MCost = [ [ 0 for i in range(N) ]  for j in range(N)]
LCity = [[] for i in range(N)]

for i in range(M):
    inputLine = [int(x) for x in input().split()]
    s = inputLine[0]
    d = inputLine[1]
    weight = inputLine[2]
    cost = inputLine[3]
    LCity[s].append(d)
    LCity[d].append(s)
    MCity[s][d] = weight
    MCity[d][s] = weight
    MCost[s][d] = cost
    MCost[d][s] = cost

AllCity = set(range(N))

def Dijkstra(source):
    path = [None for i in range(N)]
    dist = [float('inf') for i in range(N)]
    cost = [float('inf') for i in range(N)]
    Collected = set()
    dist[source] = 0
    cost[source] = 0
    while True:
        Uncollected = AllCity ^ Collected
        if len(Uncollected) == 0:
            break
        
        V = None
        ref = float('inf')
        for i in Uncollected:
            if dist[i] < ref:
                ref = dist[i]
                V = i
        if V == None:
            break

        if V == float('inf'):
            break

        Collected.add(V)

        for W in LCity[V]:
            if W not in Collected:
                if dist[V] + MCity[V][W] < dist[W]:
                    dist[W] = dist[V] + MCity[V][W]
                    cost[W] = cost[V] + MCost[V][W]
                    path[W] = V
                elif dist[V] + MCity[V][W] == dist[W] and cost[V] + MCost[V][W] < cost[W]:
                    cost[W] = cost[V] + MCost[V][W]
                    path[W] = V
    return dist,cost

dist,cost = Dijkstra(S)

print(dist[D],cost[D])