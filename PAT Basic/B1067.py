correctPSW,n = input().split()
count = 0
while 1:
    usrinput = input()
    if usrinput == '#':
        break

    if usrinput != correctPSW:
        count = count + 1
        print('Wrong password:',usrinput)
    else:
        print('Welcome in')
        break

    if count == int(n):
        print('Account locked')
        break