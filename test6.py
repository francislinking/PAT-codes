T = int(input())

for i in range(T):
    d = {}
    n = int(input())
    tarray = [int(x) for x in input().split()]
    warray = [int(x) for x in input().split()]
    for i in range(n):
        time = tarray[i]
        d[time] = d.get(time,[])
        d[time].append(warray[i])
    
    result = sum(warray)
    for k,v in d.items():
        result = result - max(v) 

    print(result)