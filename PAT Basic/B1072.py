N,M = [int(x) for x in input().split()]

tocheck = input().split()

c1 = 0
c2 = 0
for i in range(N):
    line = input().split()
    name = line[0]
    n = int(line[1])
    flag = 0
    plist = []
    for item in line[2::]:
        if item in tocheck:
            flag = 1
            c2 = c2 + 1
            plist.append(item)

    if flag == 1:
        c1 = c1 + 1
        print('{}: {}'.format(name,' '.join(plist)))

print(c1,c2)