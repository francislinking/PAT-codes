# https://qsctech-sange.github.io/1066-Root-of-AVL-Tree#%E9%A2%98%E7%9B%AE
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def rotateLeft(self):
        node = self.right
        self.right = node.left
        node.left = self
        return node

    def rotateRight(self):
        node = self.left
        self.left = node.right
        node.right = self
        return node

    def getHeight(self):
        left = 0 if not self.left else self.left.getHeight()
        right = 0 if not self.right else self.right.getHeight()
        return max(left, right) + 1

    def insert(self, val):
        if not self.val:
            self.val = val
            return self

        if self.val > val:
            self.left = Node(val) if not self.left else self.left.insert(val)
            left = 0 if not self.left else self.left.getHeight()
            right = 0 if not self.right else self.right.getHeight()
            if (left - right) == 2:
                if val >= self.left.val:
                    self.left = self.left.rotateLeft()
                self = self.rotateRight()
        else:
            self.right = Node(val) if not self.right else self.right.insert(val)
            left = 0 if not self.left else self.left.getHeight()
            right = 0 if not self.right else self.right.getHeight()
            if (left - right) == -2:
                if val <= self.right.val:
                    self.right = self.right.rotateRight()
                self = self.rotateLeft()
        return self


root = Node(None)
N = input()
for i in input().split():
    root = root.insert(int(i))
print(root.val)