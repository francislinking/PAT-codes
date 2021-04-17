N = int(input())

line = [int(x) for x in input().split()]

line.sort(reverse=True)
# print(line)
if min(line) > N:
    print(N)
else:
    for i in range(N):
        if line[i] <= i+1:
            print(i)
            break
