class TreeNode():
    def __init__(self,Node,Left,Right):
        self.node=Node
        self.left=Left
        self.right=Right

def BuildTree(Tnodelist):
    n = int(input())
    if n == 0:
        Root = -1
        return Root
    else:
        Root = 0
        check = [0]*n

    for i in range(n):
        Left, Right = input().split(' ')
        temp = TreeNode(i, Left, Right)
        
        if Left == '-':
            temp.left = -1
        else:
            temp.left = int(Left)
            check[temp.left] = 1
        
        if Right == '-':
            temp.right = -1
        else:
            temp.right = int(Right)
            check[temp.right] = 1
        
        Tnodelist.append(temp)

    for i in range(n):
        if(check[i] == 0):
            Root = i
            break
    
    return Root


def LevelTraversal(Tnodelist,Root):
    Length = len(Tnodelist)
    if Length == 0:
        return 'Empty Tree'
    else:
        QueueList = [Root]
        LeafNode = []

    while(len(QueueList) != 0):
        temp = QueueList[0]
        Left = Tnodelist[temp].left
        Right = Tnodelist[temp].right
        if Tnodelist[temp].left == Tnodelist[temp].right == -1:
            LeafNode.append(Tnodelist[temp].node)
        #print(Tnodelist[temp].node)
        del QueueList[0]
        if Left != -1:
            QueueList.append(Left)
        if Right != -1:
            QueueList.append(Right)
    
    return LeafNode

inputNodeList = []
Root = BuildTree(inputNodeList)
LeafNode = LevelTraversal(inputNodeList,Root)
print(' '.join(map(str,LeafNode)))
