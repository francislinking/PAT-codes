N = int(input())
idList = ['','A','B','C','D']
for i in range(N):
    line = input().split()
    for item in line:
        sid,ans = item.split('-')
        if ans == 'T':
            print(idList.index(sid),end='')