# reference http://blog.rainy.im/2016/06/29/huffman-encoding-in-lisp-and-python/
class Node(object):
    def __init__(self, symbol='', weight=0, path=0):
        self.left = None
        self.right = None
        self.symbol = symbol
        self.weight = weight
        self.path = path

def huffman_tree(frequency):
  SIZE = len(frequency)
  nodes = [Node(char, frequency.get(char)) for char in frequency.keys()]
  for _ in range(SIZE - 1):
    nodes.sort(key=lambda n: n.weight) # sort by weight
    left = nodes.pop(0)
    right = nodes.pop(0)
    parent = Node('', left.weight + right.weight)
    parent.left = left
    parent.right = right
    nodes.append(parent)
  return nodes.pop()

def generatePath(root):
    if root.left != None:
        root.left.path = root.path + 1
        generatePath(root.left)
    if root.right != None:
        root.right.path = root.path + 1
        generatePath(root.right)

def calcWPL(root):
    global stdWPL
    if root.symbol != '':
        stdWPL += root.weight*root.path
    if root.left != None:
        calcWPL(root.left)
    if root.right != None:
        calcWPL(root.right)

def hasPrefix(CodeList):
    CodeList.sort(key = lambda x:len(x),)
    for i in range(N):
        cmpCode = list(CodeList[i])
        cmpLength = len(cmpCode)
        j = i+1
        while j < N:
            if cmpCode == list(CodeList[j])[:cmpLength]:
                return 1
            else:
                j +=1
    return 0

#get input
N = int(input())
charLine = input().split()
freqDict = {}
for i in range(N):
    freqDict[charLine[2*i]] = int(charLine[2*i+1])

root = huffman_tree(freqDict)

#generate Path for nodes
root.path = 0
generatePath(root)

# calc standard WPL
stdWPL = 0
calcWPL(root)


# process sutdent answer
nStudent = int(input())

while nStudent != 0:

    thisWPL = 0
    CodeList = [None]*N
    for i in range(N):
        thisChar, thisCode = input().split()
        thisWPL += freqDict.get(thisChar)*len(thisCode)
        CodeList[i] = thisCode

    if(thisWPL == stdWPL and hasPrefix(CodeList) == 0):
        print('Yes')
    else:
        print('No')

    nStudent -=1