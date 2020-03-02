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
        Node, Left, Right = input().split(' ')
        temp = TreeNode(Node, Left, Right)
        
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

def isOmorphic(Tnodelist1,Root1,Tnodelist2,Root2):

    if Root1 == Root2 == -1:
        return True
    elif (Root1 == -1 and Root2 != -1) or (Root1 != -1 and Root2 == -1):
        return False
    elif Tnodelist1[Root1].node != Tnodelist2[Root2].node :
        return False
    else:
        Flag1 = isOmorphic(Tnodelist1,Tnodelist1[Root1].left,Tnodelist2,Tnodelist2[Root2].left)
        Flag2 = isOmorphic(Tnodelist1,Tnodelist1[Root1].right,Tnodelist2,Tnodelist2[Root2].right)
        Flag3 = isOmorphic(Tnodelist1,Tnodelist1[Root1].left,Tnodelist2,Tnodelist2[Root2].right)
        Flag4 = isOmorphic(Tnodelist1,Tnodelist1[Root1].right,Tnodelist2,Tnodelist2[Root2].left)

        return (Flag1 and Flag2) or (Flag3 and Flag4)

Tnodelist1 = []
Tnodelist2 = []

Root1 = BuildTree(Tnodelist1)
Root2 = BuildTree(Tnodelist2)

if isOmorphic(Tnodelist1,Root1,Tnodelist2,Root2):
    print('Yes')
else:
    print('No')