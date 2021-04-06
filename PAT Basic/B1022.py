a,b,d = map(int,input().split())

c = a + b
p = []
while(c):
    p.append(c%d)
    c = c // d

# p.reverse()
# out = 0
# for x in p:
#     out = out*10 + int(x)

L = len(p)
s = 0
for i in range(L):
    s = s + p[i]*10**i

print(s) 