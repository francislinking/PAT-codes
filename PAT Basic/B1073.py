class answer:
    def __init__(self,point,nAll,nRight,option):
        self.point  = point
        self.nAll   = nAll
        self.nRight = nRight
        self.option = option
        self.eCount = [0]*nAll  

N,M = [int(x) for x in input().split()]
answer_array = [None]*M
d = {}

# XOR to process

for i in range(M):
    # print(i)
    line    = input().split()
    point   = int(line[0])
    nAll    = int(line[1])
    nRight  = int(line[2])
    option  = set(line[3::])
    answer_array[i] = answer(point,nAll,nRight,option)

# for obj in answer_array:
#     print(obj.point,obj.nAll,obj.nRight,obj.option)

for i in range(N):
    grades = 0
    line = input().replace('(','').split(')')
    for index,item in enumerate(answer_array):
        Ans     = line[index].split()
        nAns    = int(Ans[0])
        opt     = set(Ans[1::])
        
        nRight = item.nRight
        optRight = item.option
        g = item.point

        if opt == optRight:
            grades += g
            # print('All Right')
        else:

            if opt.issubset(optRight):
                grades += g/2
                # print('Part Right')

            optError1 = opt.difference(optRight)
            optError2 = optRight.difference(opt)
            optError = optError1.union(optError2)
            # print('Error')
            for x in optError:
                name = str(index+1)+'-'+x
                d[name] = d.get(name,0) + 1


        # if nAns > nRight:
            
        #     print('error')
        # elif nAns == nRight and opt == optRight:
        #     grades += g
        #     print('All Right')
        # else:
        #     if set(opt).issubset(set(optRight)):
        #         grades += g/2
        #         print('part right')
        #     else:

        #         print('error')

    print('{:.1f}'.format(grades))

if d:
    dlist = sorted(d.items(),key=lambda k:(-k[1],k[0]))
    maxError = dlist[0][1]
    for k,v in dlist:
        if v < maxError:
            break
        else:
            print(v,k)
else:
    print('Too simple')