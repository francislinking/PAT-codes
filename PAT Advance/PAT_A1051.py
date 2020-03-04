M, N, K = map(int,input().split(' '))

std_list = [x for x in range(N+1)]

while K:
    K -=1
    input_list = [int(x) for x in input().split(' ')]
    # input_list = [5,6,4,3,7,2,1]
    stack = [0]
    i = 1
    j = 0
    while(len(stack)<=M+1):
        if stack[-1] == input_list[j]:
            stack.pop()
            j+=1
            if j == N:
                print('YES')
                break
        else:
            if i <= N:
                stack.append(std_list[i])
                i+=1
            else:
                break
    if j != N:
        print('NO')        
    