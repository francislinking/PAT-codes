N=int(input())
Line = [int(x) for x in input().split()]

HashMap = [[] for i in range(N)]
InDegree = [0]*N

for index in range(N):
    num = Line[index]
    if num > 0:
        index_p = num%N
        while ( index_p != index ):
            if Line[index_p] >0:
                HashMap[index_p].append(index)
                InDegree[index] = InDegree[index]+1
            index_p+=1
            if index_p ==N:
                index_p =0
            
Queue = []
for index in range(N):
    if InDegree[index] == 0 and Line[index] > 0:
        Queue.append(Line[index])

result = []

while(Queue):
    Queue.sort()
    temp = Queue.pop(0)
    result.append(str(temp))
    index = Line.index(temp)
    for item in HashMap[index]:
        InDegree[item]-=1
        if InDegree[item] == 0:
            Queue.append(Line[item])


print(' '.join(result))
