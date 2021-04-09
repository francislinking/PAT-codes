https://blog.csdn.net/xutiantian1412/article/details/90521916

d,N = input().split()
N = int(N)
for i in range(N-1):
    temp = ''
    L = len(d)
    index = 0
    while index < L:
        pch = d[index]
        count  = 1
        while index + 1 < L and d[index + 1] == pch:
            index = index + 1
            count = count + 1
        temp = temp + pch
        temp = temp + str(count)
        index = index + 1
    d = temp
print(d)        
