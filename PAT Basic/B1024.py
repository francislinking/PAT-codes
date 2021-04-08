line = input()
A,B = list(line.split('E'))

sign1 = A[0]
a = list(A[1::])
a.pop(a.index('.'))

sign2 = B[0]
b = int(B[1::])

if sign1 == '-':
    result = ['-']
else:
    result = []

if sign2 == '-':
    result.extend('0.')
    result.extend('0'*(b-1))
    result.extend(a)
else:
    l = len(a)
    # print all of a 
    if b < l-1:
        result.extend(a[0:b+1])
        result.extend('.')
        result.extend(a[b+1::])
    # print enough '0'
    else:
        result.extend(a)
        result.extend('0'*(b-l+1))
    
print(''.join(result))