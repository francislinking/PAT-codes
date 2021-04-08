# Zlist = [0,1,2,3,4,5,6,7,8,9,10]
Mlist = [1,0,10,9,8,7,6,5,4,3,2]
weight = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]

def isTrue(line):
    s = 0
    for i in range(17):
        # not digit
        if line[i].isdigit():
            s = s + int(line[i])*weight[i]
        else:
            return False
    
    m = Mlist[s%11]
    ch = int(line[-1]) if line[-1]!='X' else 10

    return m == ch


N = int(input())

flag = 0
for i in range(N):
    line = input()
    if not isTrue(line):
        flag = 1
        print(line)


if flag == 0:
    print('All passed')