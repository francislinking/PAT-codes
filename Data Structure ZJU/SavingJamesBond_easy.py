'''
用邻接表存图，深度优先搜索，值判断能否到岸，不需要给出路径
注意点：
计算第一步能到达的点需要加上岛的半径
'''
N, D = map(int,input().split())

LGraph = [ [] for i in range(N)]
for i in range(N):
    x, y = map(int,input().split()) 
    LGraph[i] = [x,y,0]

# LGraph = [[25, -15, 0], [-25, 28, 0], [8, 49, 0], [29, 15, 0], [-35, -2, 0], [5, 28, 0], [27, -29, 0], [-8, -28, 0], [-20, -35, 0], [-25, -20, 0], [-13, 29, 0], [-30, 15, 0], [-35, 40, 0], [12, 12, 0]]
# D = 20

Origin = [0,0,0]

def distance(v1,v2):
    x1 = v1[0]
    y1 = v1[1]
    x2 = v2[0]
    y2 = v2[1]
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def toCoast(vertex):
    x = vertex[0]
    y = vertex[1]
    return min(abs(x-50),abs(x+50),abs(y-50),abs(y+50))

def visited(vertex):
    if vertex[-1] == 0:
        return True
    else:
        return False 

def DFS(vertex,G):
    vertex[-1] = 1
    if toCoast(vertex) <= D:
        return 1
    else:
        for item in G:
            if visited(item) and distance(vertex,item) <= D:
                answer = DFS(item,G)
                if answer == 1:
                    return 1
    return 0

def save007(G):
    answer = 0
    for item in G:
        if visited(item) and distance(Origin,item)<=D+15/2:
            answer = DFS(item,G)
            if answer == 1:
                break
    if answer == 1:
        print('Yes')
    else:
        print('No')

save007(LGraph)