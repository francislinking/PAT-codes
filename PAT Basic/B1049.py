N = int(input())

line = [float(x) for x in input().split()]

s = 0
# for i in range(N):
#     # print(i)
#     for j in range(i+1,N+1):
#         s = s + sum(line[i:j])
#         # print(sum(line[i:j]))

for i in range(N):
    s = s + line[i]*()

print('{:.2f}'.format(s))