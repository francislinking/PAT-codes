A = input()
B = input()
d = {}
e = {}
for x in B:
    d[x] = d.get(x,0) + 1

for y in A:
    try:
        if d.get(y) != 0:
            d[y] = d.get(y) - 1
        else:
            e[y] = e.get(y,0) + 1
    except:
        e[y] = e.get(y,0) + 1

s = sum(d.values())
r = sum(e.values())
if s == 0:
    print('Yes',r)
else:
    print('No',s)
