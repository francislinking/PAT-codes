
T = int(input())

while(T):
    n,m = [int(x) for x in input().split()]
    fama = [int(x) for x in input().split()]
    flag = 0
    for i in range(n):
        tempsum = sum(fama[n-i::])
        for item in fama[0:n-i]:
            if (item + tempsum) % m ==0:
                flag = 1
                print(1)
                break
            if flag == 1:
                break
        if flag == 1:
            break

    if flag == 0:
        print(-1)
    T = T - 1