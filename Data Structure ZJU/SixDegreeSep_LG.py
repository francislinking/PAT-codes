'''
邻接表存图
广度优先搜索模板
超时
'''


N, M = map(int,input().split())

LGraph=[ [] for i in range(N+1) ]

for i in range(M):
    x, y = map(int,input().split())
    LGraph[x].append(y)
    LGraph[y].append(x)


def BFS(vertex):
    Queue = []
    visited = [0]*(N+1)
    visited[vertex] = True
    Queue.append(vertex)
    count = 1
    level = 0
    tail = 0
    last = vertex
    while Queue:
        vQ = Queue.pop(0)
        for item in LGraph[vQ]:
            if visited[item] != True:
                visited[item] = True
                Queue.append(item)
                count +=1
                tail = item

        if vQ == last:
            level+=1
            last = tail

        if level == 6:
            break
    return count
                


for item in range(1,N+1):
    count = BFS(item)
    print('{}: {:.2f}%'.format(item,100*count/N))