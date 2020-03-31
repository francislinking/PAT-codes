'''
字符串处理
'''
inputList = input().split(' ')
string = input().split(' ')
N = int(inputList[0])
M = int(inputList[1])
result = string[N-M:] + string[:N-M]
print(' '.join(result))