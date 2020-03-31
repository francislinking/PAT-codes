inputList = list(map(int,input().split()))

def fun1(lt):
    if not(lt):
        return 'N'
    else:
        return str(sum(lt))

def fun2(lt):
    if not(lt):
        return 'N'
    else:
        r = 0
        for i in range(len(lt)):
            if i%2==0:
                r+=lt[i]
            else:
                r-=lt[i]
        return str(r)

def fun3(lt):
    if not(lt):
        return 'N'
    else:
        return str(len(lt))

def fun4(lt):
    if not(lt):
        return 'N'
    else:
        ave = sum(lt)/len(lt)
        return str(round(ave, 1))

def fun5(lt):
    if not(lt):
        return 'N'
    else:
        return str(max(lt))


A1 = []
A2 = []
A3 = []
A4 = []
A5 = []


for i in inputList[1::]:
    iMod = i%5
    if iMod == 0 and i%2 ==0:
        A1.append(i)
    if iMod == 1:
        A2.append(i)
    if iMod == 2:
        A3.append(i)
    if iMod == 3:
        A4.append(i)
    if iMod == 4:
        A5.append(i)


result = [fun1(A1),fun2(A2),fun3(A3),fun4(A4),fun5(A5)]

print(' '.join(result))
