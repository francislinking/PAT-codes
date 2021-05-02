def judge(a,b):
    l = len(a)
    if l %2 == 1:
        return a == b
    else:
        a1 = a[:l//2]
        a2 = a[l//2::]
        b1 = b[:l//2]
        b2 = b[l//2::]
        return (judge(a1,b1) and judge(a2,b2) )or (judge(a1,b2) and judge(a2,b1))

N = int(input())

for i in range(N):
    line1 = input()
    line2 = input()
    l = len(line1)
    if l % 2 == 1:
        if line1 == line2:
            print('YES')
        else:
            print('NO')
    else:
        if judge(line1,line2):
            print('YES')
        else:
            print('NO')

