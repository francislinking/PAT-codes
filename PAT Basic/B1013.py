def eratosthenes(n):
    IsPrime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False
    return [x for x in range(2, n + 1) if IsPrime[x]]


PrimeList = [str(x) for x in eratosthenes(200000)]

M, N = [int(x) for x in input().split()]

line = 1

while M - 1 + 10*line < N:
    first = M-1 + 10*(line-1)
    last = M-1+10*line
    print(' '.join(PrimeList[first:last]))
    line +=1

print(' '.join(PrimeList[M-1+10*(line-1):N]))