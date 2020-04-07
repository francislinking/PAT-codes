N, M = [int(x) for x in input().split()]

inDegree = [0 for x in range(N)]
# adj list for Garph
inPoint = [ [] for x in range(N)]
activeTime = [ [ 0 for x in range(N) ] for x in range(N)]


for i in range(M):
    start, end, time = map(int,input().split())
    inDegree[end] += 1
    inPoint[start].append(end)
    activeTime[start][end] = time

startPoint = [x for x in range(N) if inDegree[x]==0]
CostTime = [-1 for x in range(N)]
Queue = []
for p in startPoint:
    CostTime[p] = 0
    Queue.append(p)


count = 0

while Queue:
    vQ = Queue.pop(0)
    count += 1
    for item in inPoint[vQ]:
        inDegree[item] -=1
        if inDegree[item] == 0:
            Queue.append(item)
        if CostTime[item] < CostTime[vQ] + activeTime[vQ][item]:
            CostTime[item] = CostTime[vQ] + activeTime[vQ][item]

if count == N:
    print(max(CostTime))
else:
    print('Impossible')