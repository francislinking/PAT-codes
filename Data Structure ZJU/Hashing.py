def eratosthenes(n):
    IsPrime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False
    return [x for x in range(2, n + 1) if IsPrime[x]]

n=100000
Primes = eratosthenes(n)

def GetNextPrime(x):
    if x in Primes:
        TableSize = x
    else:
        for num in Primes:
            if num>M:
                TableSize = num
                break
    return TableSize

def Hashing(key,size):
    return key%size


M,N = map(int,input().split())

TableSize = GetNextPrime(M)
HashTable = [-1]*TableSize


line = [int(x) for x in input().split()]
result = []

for num in line:
    index = Hashing(num,TableSize)
    tmp_index = index
    if HashTable[tmp_index] == -1:
        HashTable[tmp_index] = 1
        result.append(str(index))
    else:
        flag = 0
        for count in range(1,TableSize):
            index = Hashing(tmp_index+count*count,TableSize)
            if HashTable[tmp_index] == -1:
                flag = 1
                HashTable[tmp_index] = 1
                result.append(str(index))
                break
        if flag == 0:
            result.append('-')


print(' '.join(result))