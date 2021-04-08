N,M = [int(x) for x in input().split()]

record = [None]*N

for i in range(N):
    record[i] = input().split()

for j in range(1,M+1):
    itype,instruct = input().split()
    print('Case '+str(j)+': '+itype+' '+instruct)
    
    if itype == '1':
        record = sorted(record,key=lambda x: (x[1],x[0]))
        flag = 0
        for item in record:
            if item[0][0] == instruct:
                flag = 1
                print(' '.join(item))
        if flag == 0:
            print('NA')

    if itype == '2':
        count = 0
        score = 0
        for item in record:
            if item[0][1:4] == instruct:
                count = count + 1
                score = score + int(item[1])

        if count != 0:
            print(count,score)
        else:
            print('NA')

    if itype == '3':
        d={}
        for item in record:
            if item[0][4:10] == instruct:
                room = item[0][1:4]
                d[room] = d.get(room,0) + 1

        if len(d) != 0:
            result = sorted(d.items(),key = lambda x:(-x[1],x[0]))
            for item in result:
                print(item[0],item[1])
        else:
            print('NA')

