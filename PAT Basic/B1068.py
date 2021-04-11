def judge(x,y,TOL):
    thisdata = array2d[y][x]

    coord = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for item in coord:
        xx = x + item[0]
        yy = y + item[1]
        if 0 <= xx < M and 0 <= yy < N and abs(array2d[yy][xx] - thisdata) <=TOL:
            return False

    if arraydict[thisdata] == 1: 
        return True

M,N,TOL = [int(x) for x in input().split()]

array2d = [[None]*M]*N
arraydict = {}


for i in range(N):
    array2d[i] = [int(x) for x in input().split()]
    for item in array2d[i]:
        arraydict[item] = arraydict.get(item,0) + 1


count = 0
for x in range(M):
    for y in range(N):
        if judge(x,y,TOL):
            count = count + 1
            lox = x
            loy = y

if count == 0:
    print('Not Exist')
elif count == 1:
    print('({}, {}): {}'.format(lox+1,loy+1,array2d[loy][lox]))
else:
    print('Not Unique')
