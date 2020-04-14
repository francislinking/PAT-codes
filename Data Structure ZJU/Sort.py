def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubble(A, N):
    for P in range(N)[::-1]:
        flag = 0
        for i in range(P):
            if A[i] > A[i+1]:
                swap(A,i,i+1)
                flag = 1
        if flag == 0:
            break

def insertion_sort(A,left,right):
    for P in range(left+1,right+1):
        temp = A[P]
        i = P
        while(i>left and A[i-1]>temp):
            A[i] = A[i-1]
            i-=1
        A[i] = temp


def insertion(A, N):
    insertion_sort(A,0,N-1)

def shell(A, N):
    D = N//2
    while(D): 
        P=D
        while(P<N):
            temp = A[P]
            i=P
            while(i>=D and A[i-D]>temp):
                A[i] = A[i-D]
                i-=D
            A[i] = temp
            P+=1
        D //=2

def selection(A, N):
    for i in range(N):
        minItem = A[i]
        minIndex = i
        for j in range(i,N):
            if A[j] < minItem:
                minItem = A[j]
                minIndex = j
        swap(A,i,minIndex)

def PercDown(A,i,N):
    child = 2*i+1

    if (child <N-1) and (A[child]<A[child+1]):
        child +=1
    if (child <N) and (A[i] < A[child]):
        swap(A,i,child)
        PercDown(A,child,N)

def heapSort1(A, N):
    for i in range(N//2)[::-1]:
        PercDown(A,i,N)
    for i in range(N)[::-1]:
        swap(A,0,i)
        PercDown(A,0,i)

def Merge(A,tempA,L,R,rightEnd):
    leftEnd = R-1
    ptr = L
    Num = rightEnd - L +1
    while (L<=leftEnd and R<=rightEnd):
        if A[L]<=A[R]:
            tempA[ptr] = A[L]
            ptr+=1
            L+=1
        else:
            tempA[ptr] = A[R]
            ptr+=1
            R+=1
    while (L<=leftEnd):
        tempA[ptr] = A[L]
        ptr+=1
        L+=1
    while (R<=rightEnd):
        tempA[ptr] = A[R]
        ptr+=1
        R+=1
    index = 0
    while index < Num:
        A[rightEnd] = tempA[rightEnd]
        rightEnd-=1
        index+=1

def Msort(A,tempA,left,rightEnd):
    if left<rightEnd:
        mid = (left + rightEnd)//2
        Msort(A,tempA,left,mid)
        Msort(A,tempA,mid+1,rightEnd)
        Merge(A,tempA,left,mid+1,rightEnd)

def mergeSort(A, N):
    tempA = [0]*N
    Msort(A,tempA,0,N-1)

def Median3(A,left,right):
    mid = (left+right)//2
    if A[left] > A[mid]:
        swap(A,left,mid)
    if A[left] > A[right]:
        swap(A,left,right)
    if A[mid] > A[right]:
        swap(A,mid,right)
    swap(A,mid,right-1)
    return A[right-1]

def quick_Sort(A,left,right):
    if  right - left >=50:
        pivot = Median3(A,left,right)
        i = left+1
        j = right-2
        while(1):
            while(i<=right-1 and A[i] < pivot):
                i+=1
            while(j>=0 and A[j] > pivot):
                j-=1
            if i<j:
                swap(A,i,j)
            else:
                break

        swap(A,i,right-1)
        quick_Sort(A,left,i-1)
        quick_Sort(A,i+1,right)
    else:
        insertion_sort(A,left,right)

def quickSort(A, N):
    quick_Sort(A,0,N-1)

def radixSort(A, N):
    bucket = [[]for i in range(10)]
    for i in range(1,5):
        for item in A:
            sDigit = item%(10**i)//(10**(i-1))
            bucket[sDigit].append(item)

        del A[:]
        for eachBucket in bucket:
            A.extend(eachBucket) 
        bucket = [[]for i in range(10)]


N = int(input())
List = [int(x) for x in input().split()]

# bubble(List,N)
# insertion(List,N)
# shell(List,N)
# selection(List,N)
# heapSort1(List,N)
# mergeSort(List,N)
# quickSort(List,N)
radixSort(List,N)
print(' '.join([str(x) for x in List]))