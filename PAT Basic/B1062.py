def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(a%b,b) if a > b else gcd(b,a)

# def PrimeList(n):
#     IsPrime = [True]*(n+1)
#     for i in range(2,int(n**0.5)+1):
#         if IsPrime[i]:
#             for j in range(i*i, n+1, i):
#                 IsPrime[j] = False
#     return [x for x in range(2,n+1) if IsPrime[x]]

X,Y,Z = input().split()
x = eval(X)
y = eval(Y)
z = int(Z)

if x > y:
    x,y=y,x

result = []
for i in range(1,z+1):
    if gcd(i,z) == 1 and x < i/z < y:
        result.append('{}/{}'.format(i,z))

print(' '.join(result))

