A,B = input().split()

l = max(len(A),len(B))
A = A.rjust(l,'0')[::-1]
B = B.rjust(l,'0')[::-1]

result = []
for i in range(l):
    a = int(A[i])
    b = int(B[i])
    if i % 2 == 0:
        c = (a + b) % 13
    else:
        if b >= a:
            c = b - a 
        else:
            c = b - a + 10
            
    if c < 10:
        result.append(str(c))
    elif c == 10:
        result.append('J')
    elif c == 11:
        result.append('Q')
    elif c == 12:
        result.append('K')    



print(''.join(result[::-1])  )
