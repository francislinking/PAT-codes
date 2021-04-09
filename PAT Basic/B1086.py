A,B = [int(x) for x in input().split()]

C = A*B
str_c = str(C)
print(int(str_c[::-1]))