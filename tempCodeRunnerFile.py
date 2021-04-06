T = int(input())

while(T):
    n,m = [int(x) for x in input().split()]
    fama = [int(x) for x in input().split()]
   
    for item in fama:
        if item % m == 0:
            print(1)

    for item in fama[0:n-1]:
        if (item + fama[n]) % m ==0:
            print(1)

    print(-1)
    T = T - 1