# https://www.geeksforgeeks.org/check-given-binary-tree-follows-height-property-red-black-tree/

class Node:
# Initial
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def getMaxDepth(self):
        if self.data == None:
            return 0
        else:
            lmaxDepth = 0 if not self.left else self.left.getMaxDepth()
            rmaxDepth = 0 if not self.right else self.right.getMaxDepth()
            return max(lmaxDepth,rmaxDepth) + 1

    def getMinDepth(self):
        if self.data == None:
            return 0
        else:
            lminDepth = 0 if not self.left else self.left.getMinDepth()
            rminDepth = 0 if not self.right else self.right.getMinDepth()
            return min(lminDepth,rminDepth) + 1

K = int(input())
while(K!=0):
    N = int(input())
    postorder  = [ int(x) for x in input().split()]
    postorder.reverse()

    root = Node(None)
    for item in postorder:
        root.insert(item)

    MaxDepth = root.getMaxDepth()
    MinDepth = root.getMinDepth()


    if MaxDepth <= MinDepth*2 : 
        print("Yes") 
    else: 
        print("No") 
    
    K = K-1