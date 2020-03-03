def addSubNode(PostOrder, InOrder):
    SubNode = []

    root = PostOrder[-1]
    index = InOrder.index(root)

    SubLeft_InOrder = InOrder[:index]
    SubLeft_PostOrder = PostOrder[:index]
    SubRight_InOrder = InOrder[index+1:]
    SubRight_PostOrder = PostOrder[index:-1]
    
    if index !=0:
        SubNode.append((SubLeft_PostOrder,SubLeft_InOrder))
    if index != len(InOrder)-1:
        SubNode.append((SubRight_PostOrder,SubRight_InOrder))

    return root, SubNode


N = int(input())
PostOrder = list(map(int,input().split(' ')))
InOrder = list(map(int,input().split(' ')))

result = []

Left_Right = [(PostOrder,InOrder)]

while(len(Left_Right)):
    subnode = []
    for node in Left_Right:
        root, newsubnode = addSubNode(node[0], node[1])
        subnode = subnode + newsubnode
        result.append(root)
    Left_Right = subnode
    

print(' '.join(map(str,result)))