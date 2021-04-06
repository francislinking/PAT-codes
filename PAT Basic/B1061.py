N, M = [int(x) for x in input().split()]
score = [int(x) for x in input().split()]
slist = [[]*M]*N
answer = [int(x) for x in input().split()]
for i in range(N):
    slist[i] =[int(x) for x in input().split()]



for i in range(N):
    result = 0
    for j in range(M):
        if slist[i][j] == answer[j]:
            result = result + score[j]
    print(result)