N = int(input())
d = {}
for i in range(N):
    eid,js,ks = [int(x) for x in input().split()]
    d[js] = (eid,ks)

M = int(input())

line = [int(x) for x in input().split()]

for js in line:
    print(d[js][0],d[js][1])