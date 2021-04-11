'''
正则表达式
'''
import re  

# N = int(input())
# while N:

#     inputList=input()  
#     if re.match(r'A*PA+TA*',inputList): 
#         splitList=re.split(r'[P|T]',inputList)  
#         if splitList[0]*len(splitList[1])==splitList[2]:  
#             print('YES')  
#         else:  
#             print('NO')  
#     else:  
#         print('NO')

#     N -=1

N = int(input())

for i in range(N):
    line = input()
    index = 0
    invalidchar = 0
    d = {'P':0,'A':0,'T':0}
    for ch in line:
        if ch in d:
            d[ch] = d.get(ch) + 1
        else:
            invalidchar = 1
            break
        if ch == 'P':
            p = index
        if ch == 'T':
            t = index
        index = index + 1
        
    if invalidchar == 1:
        print('NO')
    elif d['P'] == 1 and d['T'] == 1 and d['A'] >=1 and p*(t-p-1) == index - t - 1:
        print('YES')
    else:
        print('NO')
