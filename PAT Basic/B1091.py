M = int(input())
toTest = [int(x) for x in input().split()]

for num in toTest:
    flag = 0
    for n in range(1,10):
        temp = n*num**2
        str_temp = list(str(temp))
        str_temp.reverse()
        str_num = list(str(num))
        str_num.reverse()
        i = 0
        while(str_num[i] == str_temp[i]):
            i = i + 1
            if i == len(str_num):
                flag = 1
                print(n,temp)
                break
        if flag == 1:
            break

    if flag == 0:
        print('No')
        
        