A = list(input())
B = list(input())
A.extend(B)

# d = {}
# for ch in A:
#     d[ch] = d.get(ch,0) + 1
#     if d[ch] == 1:
#         print(ch,end='')

d = []
for ch in A:
    if ch not in d:
        print(ch,end='')
        d.append(ch)