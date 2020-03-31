'''
参考六度分隔
广度优先搜索，增加层号记录
'''

N, L = map(int,input().split())

LGraph = [ [] for i in range(N+1)]

for item in range(1,N+1):
    inputLine = list(map(int,input().split()))
    if inputLine[0] != 0:
        for user in inputLine[1::]:
            LGraph[user].append(item)

UserID = list(map(int,input().split()))

# N,L = 7,3
# LGraph = [[], [4], [1], [1, 4, 5], [1, 5, 6], [3, 7], [3], []]
# UserID = [2, 2, 6]


def BFS(vertex):
    visited = [0]*(N+1)
    Queue = []
    visited[vertex] = True
    Queue.append(vertex)
    count = 0
    level = 0
    tail = 0
    last = vertex
    while Queue and level<L:
        vQ = Queue.pop(0)
        for item in LGraph[vQ]:
            if visited[item] != True:
                Queue.append(item)
                visited[item] = True
                count += 1
                tail = item
        
        if vQ == last:
            level+=1
            last = tail

        if level == 6:
            break

    return count


for user in UserID[1::]:
    print(BFS(user))