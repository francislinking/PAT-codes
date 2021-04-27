number = [int(x) for x in input().split()]

l = number[0] - 1

s = sum(number[1::])

result = 11*s*l

print(result)