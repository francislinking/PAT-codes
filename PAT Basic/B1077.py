N,M = [int(x) for x in input().split()]

for i in range(N):
    line = [int(x) for x in input().split()]
    s = line[1::]
    v = []
    G2 = line[0]

    for g in s:
        if 0 <= g <= M:
            v.append(g)
    v.sort()
    l = len(v)
    G1 = (sum(v[1:l-1])/(l-2))

    result = (G1+G2)/2
    if result*10%10 >= 5:
        result = int(result + 1)
    else:
        result = int(result)
    print(result)

