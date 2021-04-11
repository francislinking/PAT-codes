def Callatz(N):
    if N%2 == 0:
        N //=2
    else:
        temp = 3*N+1
        N = temp//2
    return N

N = int(input())

# inputList = list(map(int,input().split(' ')))
# inputSet = set(inputList)

# CallatzList = []
# for n in inputList:
#     while n!=1:
#         n = Callatz(n)
#         CallatzList.append(n)

# CallatzSet = set(CallatzList)

# diffSet = inputSet.difference(CallatzSet)

# diffList = list(diffSet)
# diffList.sort(reverse=True)
# print(' '.join([str(x) for x in diffList]))

line = [int(x) for x in input().split()]
d = {}
for n in line:
    while n!=1:
        n = Callatz(n)
        d[n] = d.get(n,0) + 1

result = []
for n in line:
    if n not in d.keys():
        result.append(n)

result.sort(reverse=True)
print(' '.join([str(x) for x in result]))