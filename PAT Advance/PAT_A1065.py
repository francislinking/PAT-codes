N = int(input())

index = 1
while(index<=N):
    flag = 0
    a, b, c = map(int,input().split(' '))
    if a>0 & b>0 & a+b<0:
        flag = 1
    elif a<0 & b<0 & a+b>=0:
        flag = 0
    elif a+b>c:
        flag = 1
    print('Case #{}:'.format(index),"true" if flag else "false")
    index +=1