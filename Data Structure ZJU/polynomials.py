p1 = list(input().split())
p2 = list(input().split())

d1 = {}
d1c = {}
d2 = {}
d2c = {}

d3 = {}
d4 = {}

list1 = []
list2 = []

for i in range(1,len(p1),2):
    if int(p1[i]) !=0:
        d1[int(p1[i+1])] = int(p1[i])
for i in range(1,len(p2),2):
    if int(p2[i]) !=0:
        d2[int(p2[i+1])] = int(p2[i])
    
#polu multi    
d1c = d1.copy()
d2c = d2.copy()
for k1 in d1c:
    for k2 in d2c:
        temp = d4.get(k1+k2,0) + d1c.get(k1)*d2c.get(k2)
        if temp !=0:
            d4[k1+k2] = temp
        else:
            del d4[k1+k2]
            
if len(d4) != 0:            
    for i in sorted(d4.keys(),reverse = True):
        list1.append(str(d4[i]))
        list1.append(str(i))
else:
    list1.append(str(0))
    list1.append(str(0))




#poly plus
d3 = d2.copy()
for k1 in d1:
    temp = d3.get(k1,0) + d1.get(k1)
    if (temp!=0):
        d3[k1] = temp
    else:
        del d3[k1]

if len(d3) != 0: 
    for i in sorted(d3.keys(),reverse = True):
        list2.append(str(d3[i]))
        list2.append(str(i))
else:
    list2.append(str(0))
    list2.append(str(0))

print(' '.join(list1))
print(' '.join(list2)) 