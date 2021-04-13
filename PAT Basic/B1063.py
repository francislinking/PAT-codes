def radius(x,y):
    return (x**2 + y**2)**0.5

N = int(input())

result = 0
for i in range(N):
    a,b = [int(x) for x in input().split()]
    r = radius(a,b)
    if r >= result:
        result = r

print('{:.2f}'.format(result))