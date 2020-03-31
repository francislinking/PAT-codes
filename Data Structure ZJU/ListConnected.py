'''
深度优先搜索和广度优先搜索的模板
使用邻接表存图，邻接表用二维列表实现[[] ...]
'''

def DFS(vertex):
    visited[vertex] = True
    resultDFS.append(vertex)
    for item in LGraph[vertex]:
        if visited[item] != True:
            DFS(item)

def ListDFS(G):
    for vertex in range(N):
        if visited[vertex] != True:
            DFS(vertex)
            resultDFS.append(-1)

def PrintResult(lt):
    while lt:
        end = lt.index(-1)
        print('{ '+' '.join(map(str,lt[:end]))+' }' )
        lt = lt[end+1::]


def BFS(vertex):
    visited[vertex] = True
    resultBFS.append(vertex)
    Queue.append(vertex)
    while Queue:
        vQ = Queue.pop(0)
        for item in LGraph[vQ]:
            if visited[item] != True:
                Queue.append(item)
                visited[item] = True
                resultBFS.append(item)

def ListBFS(G):
    for vertex in range(N):
        if visited[vertex] != True:
            BFS(vertex)
            resultBFS.append(-1)


N, E = map(int,input().split())

LGraph=[ [] for i in range(N) ]

#Adj List
for i in range(E):
    x, y = map(int,input().split())
    LGraph[x].append(y)
    LGraph[y].append(x)

for item in LGraph:
    item.sort()


resultDFS = []
resultBFS = []
Queue = []

visited = [0]*N
ListDFS(LGraph)
PrintResult(resultDFS)

visited = [0]*N
ListBFS(LGraph)
PrintResult(resultBFS)