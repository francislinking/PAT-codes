N = int(input())

n = int(N**0.5)
while(N%n):
    n = n - 1
m = N//n 

map2d = [[0 for i in range(n)] for j in range(m)]
# []*n is shallow copy
# print(map2d)

# print(m,n)
line = [int(x) for x in input().split()]
line.sort(reverse=True)
# print(line)


index = 0

# boundary
up = 0
down = m - 1
left = 0
right = n - 1

while( index < N ):
    for i in range(left,right):
        # print(i,up,index)
        map2d[up][i] = line[index]
        index += 1 

    if index == N:
        break

    for j in range(up,down+1):
        # print(right,j,index)
        map2d[j][right] = line[index]
        index += 1

    if index == N:
        break

    for i in range(left,right)[::-1]:
        # print(i,down,index)
        map2d[down][i] = line[index]
        index += 1

    if index == N:
        break

    for j in range(up+1,down)[::-1]:
        # print(left,j,index)
        map2d[j][left] = line[index]
        index += 1

    if index == N:
        break

    up += 1
    down -= 1
    left += 1
    right -= 1


# output 
for everyline in map2d:
    print(' '.join([str(x) for x in everyline]))