N, M = [int(x) for x in input().split()]

inDegree = [0 for x in range(N)]
outDegree = [0 for x in range(N)]
# adj list for Garph
inPoint = [ [] for x in range(N)]
outPoint = [ [] for x in range(N)]
# adj matrix
activeTime = [ [ 0 for x in range(N) ] for x in range(N)]

# gei input,
for i in range(M):
    start, end, time = map(int,input().split())
    start-=1
    end-=1
    inDegree[end] += 1
    outDegree[start] += 1
    inPoint[start].append(end)
    outPoint[end].append(start)
    activeTime[start][end] = time

# find start point / inDegree == 0
startPoint = [x for x in range(N) if inDegree[x]==0]
Eariest = [-1 for x in range(N)]

# put into queue
Queue1 = []
for p in startPoint:
    Eariest[p] = 0
    Queue1.append(p)

count = 0

# Generate Eariest for each point
while Queue1:
    vQ = Queue1.pop(0)
    count += 1
    for item in inPoint[vQ]:
        inDegree[item] -=1
        if inDegree[item] == 0:
            Queue1.append(item)
        if Eariest[item] < Eariest[vQ] + activeTime[vQ][item]:
            Eariest[item] = Eariest[vQ] + activeTime[vQ][item]
lmst = max(Eariest)

# find end point / outDegree == 0
endPoint = [x for x in range(N) if outDegree[x]==0]
Latest = [lmst for x in range(N)]
Queue2 = []
for p in endPoint:
    Queue2.append(p)

# Generate Latest for each point
while Queue2:
    vQ = Queue2.pop(0)
    for item in outPoint[vQ]:
        outDegree[item] -=1
        if outDegree[item] == 0:
            Queue2.append(item)
        if Latest[item] > Latest[vQ] - activeTime[item][vQ]:
            Latest[item] = Latest[vQ] - activeTime[item][vQ]

def printKey():
    for i in range(N):
        for j in range(N)[::-1]:
            temp = activeTime[i][j]
            if temp and Latest[j] - Eariest[i] - temp== 0:
                print(str(i+1)+'->'+str(j+1))


if count == N:
    print(lmst)
    printKey()
else:
    print(0)

