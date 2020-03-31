def derivate(coe,poe):
    if coe == 0 or poe == 0:
        return 0,0
    return coe*poe,poe-1

poly=list(map(int,input().split()))

result = []

L = len(poly)
for i in range(0,L,2):
    temp = derivate(poly[i],poly[i+1])
    if temp != (0,0):
        result.append(temp[0])
        result.append(temp[1])

resultStr = [str(x) for x in result]
if resultStr:
    print(' '.join(resultStr))
else:
    print('0 0')
