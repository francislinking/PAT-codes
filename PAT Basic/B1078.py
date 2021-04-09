instruct = input()
line = input()+'\n'

L = len(line) - 1

if instruct == 'C':
    index = 0
    count = 0
    p = line[index]
    while index <= L:
        if line[index] == p:
            count = count + 1
            index = index + 1
        else:
            if count != 1:
                print(str(count),end='')
            print(str(p),end='')
            count = 0
            p = line[index]

if instruct == 'D':
    index = 0
    count = '0'
    while index < L:
        if line[index].isdigit():
            count = count + line[index]
            index = index + 1
        else:
            if count != '0':
                print(line[index]*int(count),end='')
            else:
                print(line[index],end='')
            count = '0'
            index = index + 1

        
