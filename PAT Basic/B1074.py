d = input()
a = input()
b = input()
L = max(len(d),len(a),len(b))
a = a.zfill(L)
b = b.zfill(L)
out = []

abdzip = list(zip(a,b,d))

cin = 0
for item in abdzip[::-1]:
    x,y,z = map(int,item)
    s = x + y + cin
    if z == 0:
        z = 10
    cin = s // z
    out.append(s % z)

result = 0
for i in range(L):
    result = result + out[i]*10**i

print(result)