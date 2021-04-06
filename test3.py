T = int(input())

while(T):
    left = []
    right = []
    sumtime = 0
    n = int(input())
    time = [int(x) for x in input().split()]
    time.sort()

    if (n == 3):
        sumtime = sum(time)
        print(sumtime)
    if (n == 4):
        sumtime = time[0]*3 + time[1]*2 + time[3]
        print(sumtime)

    left.append(time[0])
    left.append(time[1])
    sumtime = sumtime + time[1]
    right = time[2::]
        
    

    # print(time)

 


    T = T - 1