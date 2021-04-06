def simple(a,b):
    if (a*b == 0):
        print("Inf" if b == 0 else "0",end = '')
        return
    flag = (a>0 and b <0) or (a<0 and b>0)
    if flag:
        print('(-',end='')
    a = abs(a)
    b = abs(b)
    t = gcd(a,b)
    a = a//t
    b = b//t
    c = a//b
    a = a % b
    if c != 0:
        print(str(c),end='')
    if a != 0:
        if c!=0:
            print(' ',end='')
        print(str(a)+'/'+str(b),end='')
    if flag:
        print(')',end='')




def gcd(m,n):
    return m if n == 0 else gcd(n, m%n)
            

M, N = input().split()
# # print(type(a),type(b))

a1,b1 = map(int,M.split('/'))
a2,b2 = map(int,N.split('/'))

# +
simple(a1,b1)
print(' + ',end='')
simple(a2,b2)
print(' = ',end='')
simple(a1*b2+a2*b1,b1*b2)
print(end='\n')
# -
simple(a1,b1)
print(' - ',end='')
simple(a2,b2)
print(' = ',end='')
simple(a1*b2-a2*b1,b1*b2)
print(end='\n')
# *
simple(a1,b1)
print(' * ',end='')
simple(a2,b2)
print(' = ',end='')
simple(a1*a2,b1*b2)
print(end='\n')
# /
simple(a1,b1)
print(' / ',end='')
simple(a2,b2)
print(' = ',end='')
simple(a1*b2,a2*b1)
print(end='\n')