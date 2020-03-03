def addSubTree(PostOrder, InOrder):
    SubTreeNode = []

    root = PostOrder[-1]
    index = InOrder.index(root)

    SubLeft_InOrder = InOrder[:index]
    SubLeft_PostOrder = PostOrder[:index]
    SubRight_InOrder = InOrder[index+1:]
    SubRight_PostOrder = PostOrder[index:-1]
    
    if index !=0:
        SubTreeNode.append((SubLeft_PostOrder,SubLeft_InOrder))
    if index != len(InOrder)-1:
        SubTreeNode.append((SubRight_PostOrder,SubRight_InOrder))

    return root, SubTreeNode


N = int(input())
PostOrder = list(map(int,input().split(' ')))
InOrder = list(map(int,input().split(' ')))

result = []

Left_Right = [(PostOrder,InOrder)]

while(len(Left_Right)):
    subnode = []
    for node in Left_Right:
        root, newsubnode = addSubTree(node[0], node[1])
        subnode = subnode + newsubnode
        result.append(root)
    Left_Right = subnode
    

print(' '.join(map(str,result)))