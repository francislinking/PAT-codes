'''
正则表达式
'''
import re  

N = int(input())
while N:

    inputList=input()  
    if re.match(r'A*PA+TA*',inputList): 
        splitList=re.split(r'[P|T]',inputList)  
        if splitList[0]*len(splitList[1])==splitList[2]:  
            print('YES')  
        else:  
            print('NO')  
    else:  
        print('NO')

    N -=1