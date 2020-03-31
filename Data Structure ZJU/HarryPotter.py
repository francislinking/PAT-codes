'''
超时
思路：读取输入存入距离矩阵，初始化路径矩阵为-1
调用Floyd算法计算并更新距离矩阵和路径矩阵，寻找每个节点所有路径中的最大值，寻找这些最大值中的最小值
'''
VertexNum, EdgeNum = map(int,input().split())

# Distance Matirx
Mdist = [[float('inf') for j in range(VertexNum)] for i in range(VertexNum)]
# Path Matrix
Mpath = [[-1 for j in range(VertexNum)] for i in range(VertexNum)]

for i in range(EdgeNum):
    record = [int(x) for x in input().split()]
    Mdist[record[0]-1][record[1]-1] = record[2]
    Mdist[record[1]-1][record[0]-1] = record[2]

#Floyd 
for i in range(VertexNum):
    for j in range(VertexNum):
        for k in range(VertexNum):
            if i == j:
                Mdist[i][j] = 0
            if i!=j and Mdist[i][k] + Mdist[k][j] < Mdist[i][j]:
                Mdist[i][j] = Mdist[i][k] + Mdist[k][j]
                Mpath[i][j] = k

subMax = []

for item in Mdist:
    subMax.append(max(item))

minPath = min(subMax)

if minPath == float('inf'):
    print(0)
else:
    code = subMax.index(minPath)
    print(code+1,max(Mdist[code]))