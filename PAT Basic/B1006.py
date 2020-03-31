'''
分支结构，字符串处理
'''

num = input()
L = len(num)

Ge = []
Shi = []
Bai = []

Ge = [str(x) for x in range(1,int(num[-1])+1)]
if L >= 2:
    Shi = int(num[-2])*['S']
if L>= 3:
    Bai = int(num[-3])*['B']

output = Bai+Shi+Ge
print(''.join(output))