def Callatz(N):
    if N%2 == 0:
        N /=2
    else:
        temp = 3*N+1
        N = temp/2
    return N

N = int(input())

inputList = list(map(int,input().split(' ')))
inputSet = set(inputList)

CallatzList = []
for n in inputList:
    while n!=1:
        n = Callatz(n)
        CallatzList.append(n)

CallatzSet = set(CallatzList)

diffSet = inputSet.difference(CallatzSet)

diffList = list(diffSet)
diffList.sort(reverse=True)
print(' '.join([str(x) for x in diffList]))
