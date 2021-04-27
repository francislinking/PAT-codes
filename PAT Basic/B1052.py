shou = input().replace(']','').split('[')
yan = input().replace(']','').split('[')
kou = input().replace(']','').split('[')

N = int(input())
for i in range(N):
    indexarray = [int(x) for x in input().split()]
    try:
        zs = shou[indexarray[0]]
        zy = yan[indexarray[1]]
        k = kou[indexarray[2]]
        yy = yan[indexarray[3]]
        ys = shou[indexarray[4]]
        result = zs+'('+zy+k+yy+')'+ys
        print(result)
    except:
        print('Are you kidding me? @\/@')