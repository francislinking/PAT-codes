# def erato(n):
#     IsPrime = [True]*(n+1)
#     for i in range(2, int(n**0.5)+1):
#         if(IsPrime[i]):
#             for j in range(i*i,n+1,i):
#                 IsPrime[j] = False
#     return [x for x in range(2,n+1) if IsPrime[x]]

# PrimeList = erato(100000)
def isPrime(n):
    if (n == 0 or n == 1):
        return False
    for i in range(2,int(n**0.5)+1):
        if (n % i == 0):
            return False
    return True

N,M = list(map(int,input().split()))
line = input()

flag = 0
for i in range(0,N-M+1):
    num_str = line[i:i+M]
    num = int(num_str)
    if isPrime(num):
        flag = 1
        print(num_str)
        break

if flag == 0:
    print('404')