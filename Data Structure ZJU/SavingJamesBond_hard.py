'''
思路：
先读取点，有效点为在池里的点（不在岛上且不在岸上）
同时判断初始点（第一步能达到的点），然后将初始点的序号按照距离从小到大排序
将两个有效点（距离小于跳跃）存入邻接表
广度优先搜索模板，同时更新路径和跳跃次数，如果到岸返回最后一个点，否则返回None
由于初始点已经按距离排序，从小到大计算跳跃次数，
后面的初始点只有跳跃次数小于前面点才有可能是最优路径
将路径存入alist列表，最后反序输出
注意点：
跳跃能力极强，一步到岸
'''

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

def Valid(vertex):
    x = vertex[0]
    y = vertex[1]
    return abs(x)<=50 and abs(y)<=50 and distance(Origin,vertex)>=15/2

#get input
N, D = map(int,input().split())

ValidVertex = [ [] for i in range(N)]

# x,y,dist,path
Origin = [0,0]

FisrtJump = []

for i in range(N):
    x, y = map(int,input().split()) 
    temp = [x,y]
    if Valid(temp):
        ValidVertex.append(temp)
        if distance(Origin,temp)<=15/2+D:
            FisrtJump.append(temp)

ValidVertex = [x for x in ValidVertex if x !=[]]

if ValidVertex != []:
    FisrtJumpIndex = [ValidVertex.index(x) for x in FisrtJump]
    FisrtJumpIndex.sort(key=lambda x: distance(Origin,ValidVertex[x]))
else:
    FisrtJumpIndex = []

ValidVertexNum = len(ValidVertex)
LGraph = [ [] for i in range(ValidVertexNum)]

for i in range(ValidVertexNum):
    for j in range(ValidVertexNum):
        if i!=j and distance(ValidVertex[i],ValidVertex[j])<=D:
            LGraph[i].append(j)


def BFS(start,G):
    Queue = []
    Queue.append(start)
    dist[start] = 1
    while Queue:
        vQ = Queue.pop(0)
        for item in G[vQ]:
            if dist[item] == float('inf'):
                dist[item] = dist[vQ] + 1
                path[item] = vQ 
                Queue.append(item)
                if toCoast(ValidVertex[item])<=D:
                    return item
    return None

steps = 0
ref_steps = 1000000
alist = []

for v in FisrtJumpIndex:
    dist = [float('inf')]*ValidVertexNum
    path = [ -1 ]*ValidVertexNum
    answer = BFS(v,LGraph)
    if answer:
        steps = dist[answer] + 1
        if steps < ref_steps:
            ref_steps = steps
            alist = [answer]
            index = answer
            while path[index] != -1:
                alist.append(path[index])
                index = path[index]

if D>=50-15/2:
    print(1)
elif alist:
    print(steps)
    for i in alist[::-1]:
        print(' '.join([str(x) for x in ValidVertex[i]]))
else:
    print(0)