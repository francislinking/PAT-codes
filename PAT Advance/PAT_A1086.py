def GetInput():
    N = int(input())
    M = 2*N
    StackList = []
    InOrderList = []
    PreOrderList = []
    while(M):
        input_str = input().split(' ')
        if input_str[0] == 'Push':
            PreOrderList.append(input_str[1])
            StackList.append(input_str[1])
        elif input_str[0] == 'Pop':
            InOrderList.append(StackList.pop())
        M -= 1
    return InOrderList,PreOrderList

def PostOrderTraversal(InOrderList,PreOrderList):
    global PostOrderList
    if len(InOrderList) == len(PreOrderList) == 1:
        PostOrderList.append(PreOrderList[0])
    else:
        root = PreOrderList[0]
        index = InOrderList.index(root)
        
        SubLeft_InOrder = InOrderList[0:index]
        SubLeft_PreOrder = PreOrderList[1:index+1]
        if len(SubLeft_InOrder) == len(SubLeft_PreOrder) != 0:
            PostOrderTraversal(SubLeft_InOrder,SubLeft_PreOrder)
        
        SubRight_InOrder = InOrderList[index+1::]
        SubRight_PreOrder = PreOrderList[index+1::]
        if len(SubRight_InOrder) == len(SubRight_PreOrder) != 0:
            PostOrderTraversal(SubRight_InOrder,SubRight_PreOrder)
        PostOrderList.append(root)



PostOrderList = []
InOrder, PreOrder=GetInput()
PostOrderTraversal(InOrder, PreOrder)


print(' '.join(map(str,PostOrderList)))