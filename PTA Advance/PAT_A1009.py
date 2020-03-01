p1 = list(input().split())
p2 = list(input().split())

d1 = {}
d2 = {}
d3 = {}


list1 = []


for i in range(1,len(p1),2):
    if float(p1[i+1]) !=0:
        d1[int(p1[i])] = float(p1[i+1])
for i in range(1,len(p2),2):
    if float(p2[i+1]) !=0:
        d2[int(p2[i])] = float(p2[i+1])
        
for k1 in d1:
    for k2 in d2:
        temp = d3.get(k1+k2,0) + d1.get(k1)*d2.get(k2)
        if temp !=0:
            d3[k1+k2] = round(temp,1)
        else:
            del d3[k1+k2]
list1 = [str(len(d3))]            
if len(d3) != 0:            
    for i in sorted(d3.keys(),reverse = True):
        list1.append(str(i))
        list1.append(str(d3[i]))
else:
    list1.append(str(0))
    list1.append(str(0))

print(' '.join(list1))