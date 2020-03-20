# Heap here is MinHeap
def HeapInsert(number):
    pos = len(HeapList)
    HeapList.append(number)
    while HeapList[pos//2] > number:
        HeapList[pos] = HeapList[pos//2]
        pos = pos//2
    HeapList[pos] = number

def HeapPrint(index):
    plist = []
    while index !=0:
        plist.append(HeapList[index])
        index = index//2
    print(' '.join(map(str,plist)))

# get input
N, K = map(int,input().split())
inputList = list(map(int,input().split()))
leafList = list(map(int,input().split()))


# initial heap with guard
MinFlag = -10001
HeapList = [MinFlag]

# call function
for number in inputList:
    HeapInsert(number)

for index in leafList:
    HeapPrint(index)