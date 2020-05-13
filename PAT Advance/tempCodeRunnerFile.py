N, L = map(int,input().split())

LGraph = [ [] for i in range(N+1)]

for item in range(1,N+1):
    inputLine = list(map(int,input().split()))
    if inputLine[0] != 0:
        for user in inputLine[1::]:
            LGraph[user].append(item)

UserID = list(map(int,input().split()))