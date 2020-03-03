N = int(input())

Queue = [x for x in range(1,N+1)]
count = 1
while( len(Queue) != 1):    
    if count == 3:
        count =1
        Queue.pop(0)
    else:
        Queue.append(Queue.pop(0))
        count +=1
    
print(Queue[0])