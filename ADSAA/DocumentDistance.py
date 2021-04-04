N = int(input())
title = []
dictList = []
while N:
    while 1:
        subtitle = input()
        title.append(subtitle)
        content = input().split()
        index = title.index(subtitle)
        currentDict = dict()
        
        for words in content:
            currentDict[words] = currentDict.get(words,0) + 1 


        tail = input()
        if tail == '#':
            break
            

    N = N - 1 