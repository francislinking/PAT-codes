def isOmorphic(list1, list2):

    if len(list1) == len(list2) == 0:
        return True
    elif (len(list1) == len(list2) != 0) and (list1[0] == list2[0]):
        subLeft_1 = subLeftList(list1)
        subRight_1 = subRightList(list1)
        subLeft_2 = subLeftList(list2)
        subRight_2 = subRightList(list2)
        return isOmorphic(subLeft_1,subLeft_2) and isOmorphic(subRight_1,subRight_2)
    else:
        return False

def subLeftList(inputList):
    outputList = []
    root = inputList[0]
    for i in inputList:
        if i < root:
            outputList.append(i)
    return outputList

def subRightList(inputList):
    outputList = []
    root = inputList[0]
    for i in inputList:
        if i > root:
            outputList.append(i)
    return outputList

while(1):
    input_num = list(map(int,input().split()))
    N = input_num[0]
    if N == 0:
        break
    else:
        L = input_num[1]
        refTree = list(map(int,input().split()))
        while(L):
            compareTree = list(map(int,input().split()))
            if isOmorphic(refTree, compareTree):
                print('Yes')  
            else:
                print('No')
            L -=1
