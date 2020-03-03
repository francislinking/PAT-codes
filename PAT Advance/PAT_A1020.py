class TreeNode():
    def __init__(self,Node,Left,Right):
        self.node=Node
        self.left=Left
        self.right=Right

def BulidTree(InOrderList,PostOrderList):
    global LevelOrderList

    root = PostOrderList[-1]
    index = InOrderList.index(root)

    if index == 0:
        SubLeft_InOrder = [-1]
        SubLeft_PostOrder = [-1]
    else:
        SubLeft_InOrder = InOrderList[0:index] 
        SubLeft_PostOrder = PostOrderList[0:index]

    if index == len(PostOrderList)-1:
        SubRight_InOrder = [-1]
        SubRight_PostOrder = [-1]
    else:
        SubRight_InOrder = InOrderList[index+1::] 
        SubRight_PostOrder = PostOrderList[index:-1]


    tempNode = TreeNode(root,SubLeft_PostOrder[-1],SubRight_PostOrder[-1])
    LevelOrderList.append(tempNode)

    if SubLeft_PostOrder[-1] != -1:
        BulidTree(SubLeft_InOrder,SubLeft_PostOrder)
    if SubRight_PostOrder[-1] != -1:
        BulidTree(SubRight_InOrder,SubRight_PostOrder)

def LevelTraversal(Tnodelist,Root):
    Length = len(Tnodelist)
    if Length == 0:
        return 'Empty Tree'
    else:
        QueueList = [Root]
        LevelOrder = []

    while(len(QueueList) != 0):
        temp = QueueList[0]
        Left = Tnodelist[temp].left
        Right = Tnodelist[temp].right
        LevelOrder.append(temp)
        del QueueList[0]
        if Left != -1:
            QueueList.append(Left)
        if Right != -1:
            QueueList.append(Right)
    
    return LevelOrder


N = int(input())
LevelOrderList = []
PostOrder = list(map(int,input().split(' ')))
InOrder = list(map(int,input().split(' ')))

BulidTree(InOrder,PostOrder)
root = LevelOrderList[0].node
LevelOrderList.sort(key=lambda x: x.node)
LevelOrderList.insert(0,None)

LevelOrder = LevelTraversal(LevelOrderList,root)

print(' '.join(map(str,LevelOrder)))