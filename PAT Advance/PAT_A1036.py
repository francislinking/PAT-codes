N = int(input())
Frecord = ['','',-1]
Mrecord = ['','',101]

while(N):
    line = input().split()
    name = line[0]
    uid = line[2]
    score = int(line[3])

    if line[1] == 'F':
        if(Frecord[2]<score):
            Frecord[0] = name
            Frecord[1] = uid
            Frecord[2] = score
    else:
        if(Mrecord[2]>score):
            Mrecord[0] = name
            Mrecord[1] = uid
            Mrecord[2] = score 

    N = N - 1

if (Frecord[2] != -1):
    print(Frecord[0],Frecord[1])
else:
    print('Absent')
if (Mrecord[2] != 101):
    print(Mrecord[0],Mrecord[1])
else:
    print('Absent')

if Frecord[2] != -1 and Mrecord[2] != 101 :
    print(Frecord[2] - Mrecord[2])
else:
    print('NA')
