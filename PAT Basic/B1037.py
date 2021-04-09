# def subtract(a,b,c,d,e,f):
#     z = c - f if c > f else c + 29 - f
#     b = b if c > f else b - 1
#     y = b - e if b > e else b + 17 - e
#     x = a - d if b > e else a - 1 -d

#     return x,y,z

# P,A = input().split()

# a,b,c = [int(x) for x in P.split('.')]
# d,e,f = [int(x) for x in A.split('.')]
# # A-P, (d,e,f) - (a,b,c)
# if a > d or (a == d and b > e) or (a == d and b == e and c > f):
#     (a,b,c),(d,e,f) = (d,e,f),(a,b,c)
#     print('-',end='')

# x,y,z = subtract(d,e,f,a,b,c)
# print('{}.{}.{}'.format(x,y,z))

def GSK(a,b,c):
    return (a * 17 + b) * 29 + c

def rGSK(num):
    x,y = divmod(num//29,17)
    z = num %29
    return x,y,z

P,A = input().split()
x,y,z = [int(x) for x in P.split('.')]
l,m,n = [int(x) for x in A.split('.')]

psum = GSK(x,y,z)
asum = GSK(l,m,n)

delta = asum - psum

if delta < 0 :
    delta = - delta
    print('-',end='')

r,s,t = rGSK(delta)
print('{}.{}.{}'.format(r,s,t))