def get(ref):
    if M == ref:
        return 'Ping'
    elif M < ref:
        return 'Cong'
    else:
        return 'Gai'


M,X,Y = [int(x) for x in input().split()]
flag = 0
for a in range(10,100)[::-1]:
    b = a%10 *10 + a//10
    c = abs(a-b)/X
    if c * Y == b:
        print(a,get(a),get(b),get(c))
        flag = 1
        break

if flag == 0:
    print('No Solution')        