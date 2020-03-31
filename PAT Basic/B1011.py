N = int(input())

count = 1
while count <= N:
    inputList = list(map(int,input().split()))
    a = inputList[0]
    b = inputList[1]
    c = inputList[2]

    if a + b > c:
        print('Case #'+str(count)+': true')
    else:
        print('Case #'+str(count)+': false')

    count += 1