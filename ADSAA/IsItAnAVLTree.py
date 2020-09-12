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
        
# Print the tree in-order
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

# get Tree Height
    def getHeight(self):
        if self.data == None:
            return 0
        else:
            left = 0 if not self.left else self.left.getHeight()
            right = 0 if not self.right else self.right.getHeight()
            return max(left, right) + 1

# get Balance Factor
    def getBalanceFactor(self):
        left = 0 if not self.left else self.left.getHeight()
        right = 0 if not self.right else self.right.getHeight()
        return abs(left - right)

# judge AVL Tree
    def judgeAVL(self):
        if self.data == None:
            return True
        elif self.getBalanceFactor() > 1:
            return False
        else:
            leftAVL = True if not self.left else self.left.judgeAVL()
            rightAVL = True if not self.right else self.right.judgeAVL()
            return leftAVL and rightAVL



K = int(input())

while(K):
    N = int(input())
    preorder = [int(x) for x in  input().split()]
    
    root = Node(None)
    for item in preorder:
        root.insert(item)

    if root.judgeAVL():
        print('Yes')
    else:
        print('No')

    K = K-1

