p1 = list(input().split())
p2 = list(input().split())
d1 = {}
d2 = {}
d3 = {}
k = []

for i in range(1,len(p1),2):
    d1[int(p1[i])] = d1.get(int(p1[i]),float(p1[i+1]))
for i in range(1,len(p2),2):
    d2[int(p2[i])] = d2.get(int(p2[i]),float(p2[i+1]))

d3 = d2.copy()
for k1 in d1:
    temp = d3.get(k1,0) + d1.get(k1)
    if (temp!=0):
        d3[k1] = temp
    else:
        del d3[k1]

list1 = [str(len(d3))]

for i in sorted(d3.keys(),reverse = True):
    list1.append(str(i))
    list1.append(str(round(d3[i], 1)))
print(' '.join(list1))