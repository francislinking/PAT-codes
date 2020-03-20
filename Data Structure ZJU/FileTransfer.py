def FindRoot(c):
    index = c
    while sList[index] > 0:
        index = sList[index]
    return index

def check(c1, c2):
    r1 = FindRoot(c1)
    r2 = FindRoot(c2)
    if r1 == r2:
        print('yes')
    else:
        print('no')

def unite(c1, c2):
    r1 = FindRoot(c1)
    r2 = FindRoot(c2)
    if ( abs(sList[r1]) > abs(sList[r2]) ):
        sList[r1] -= 1
        sList[r2] = r1
    else:
        sList[r2] -= 1
        sList[r1] = r2

N = int(input())

sList=[0]+[-1]*N

while True:
    inputLine = input().split()
    cmd = inputLine[0]
    if cmd == 'S':
        rootList = [x for x in sList if x < 0]
        k = len(rootList)
        if k != 1:
            print('There are {} components.'.format(k))
        else:
            print('The network is connected.')
        break
    else:
        c1 = int(inputLine[1])
        c2 = int(inputLine[2])
        if cmd == 'I':
            unite(c1, c2)
        if cmd == 'C':
            check(c1, c2)
