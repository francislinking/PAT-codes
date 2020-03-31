'''
邻接矩阵存图
广度优先搜索模板
超时
'''

N, M = map(int,input().split())
L = (N*(N+1))//2
MGraph=[0] * L

for i in range(M):
    x, y = map(int,input().split())
    j = min(x,y)
    i = max(x,y)
    index = (i*(i-1))//2+j-1
    MGraph[index] = 1


def BFS(vertex):
    result = []
    Queue = []
    Queue.append(vertex)
    level = 0
    tail = 0
    last = vertex
    while Queue:
        vQ = Queue.pop(0)
        result.append(vQ)
        for item in ConnectedVertex(vQ):
            if item not in result and item not in Queue:
                Queue.append(item)
                tail = item

        if vQ == last:
            level+=1
            last = tail

        if level == 7:
            break
    return len(result)
                
def ConnectedVertex(vertex):
    cList = []
    for x in range(1,N+1):
        j = min(x,vertex)
        i = max(x,vertex)
        index = (i*(i-1))//2+j-1
        if MGraph[index] == 1:
            cList.append(x)
    return cList


for item in range(1,N+1):
    count = BFS(item)
    print('{}: {:.2f}%'.format(item,100*count/N))