def revadd(nonpali):
    addsum = int(nonpali) + int(nonpali[::-1])
    print(nonpali,'+',nonpali[::-1],'=',addsum)
    return str(addsum)

def isPali(inputlist):
    if inputlist == inputlist[::-1]:
        print(N,'is a palindromic number.')
        return 1
    else:
        return 0

N = input()
record = 10

for i in range(record):
    if isPali(N):
        break
    else:
        N = revadd(N)

if i == 9:
    print('Not found in 10 iterations.')
