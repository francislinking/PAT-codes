def MaxSubseqSum4(A,N):
    global ThisSum, MaxSum,start,end
    for i in range(N):
        ThisSum += A[i]
        if ThisSum > MaxSum:
            MaxSum = ThisSum
            end = i;
        elif ThisSum <= 0:
            ThisSum = 0
            start = i+1
    if MaxSum <= 0:
        print(0,A[0],A[N-1])
    else:
        print(MaxSum,start+1,end+1)
                
ThisSum = 0
MaxSum = 0
start = 0
end = 0

N = eval(input())

str_in = input()
A = list( map(int, str_in.strip().split()) )
MaxSubseqSum4(A,N)  