def BuildMatch(pattern):
    M = len(pattern)
    match = [-1]*M
    for j in range(1,M):
        i = match[j-1]
        while( i>=0 and pattern[i+1] != pattern[j] ):
            i = match[i]
        if pattern[i+1] == pattern[j]:
            match[j] = i+1
        else:
            match[j] = -1

    return match


def KMP(string,pattern):
    N=len(string)
    M=len(pattern)
    if N<M:
        return -1

    MatchArray = BuildMatch(pattern)

    s=0
    p=0

    while(s<N and p<M):
        if(string[s] == pattern[p]):
            s+=1
            p+=1
        elif p>0:
            p=MatchArray[p-1]+1
        else:
            s+=1

    if p==M:
        return s-M
    else:
        return -1

S = input()
N = int(input())
for i in range(N):
    P = input()
    index = KMP(S,P)
    if index == -1:
        print('Not Found')
    else:
        print(S[index::])