N = int(input())
d = {}
for i in range(N):
    a,b = [int(x) for x in input().split()]
    d[a] = b
    d[b] = a

M = int(input())

line = [int(x) for x in input().split()]
result = []
for people in line:
    try:
        couple = d.get(people)
        if couple not in line:
            result.append(people) 
    except:
        result.append(people)

str_result = [str(x) for x in sorted(result)]
num = len(str_result)
print(num)
if num:
    print(' '.join(str_result))