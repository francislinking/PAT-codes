d1={}
d2={}

hint_line = input().split(' ')
start_addr = hint_line[0]
L = int(hint_line[1])
K = int(hint_line[2])

for i in range(L):
    addr1, k, addr2 = input().split(' ')
    d1[addr1] = int(k)
    d2[int(k)] = addr2

res_key=[]

temp_addr = start_addr 
for i in range(L):
    res_key.append(d1[temp_addr])
    temp_addr = d2[d1[temp_addr]]
    if temp_addr == '-1':
        break

d1r={}
d2c={}

d1r = dict(zip(d1.values(),d1.keys()))

list1 = res_key[:K][::-1] + res_key[K:]


next_addr = '-1'
for i in list1[::-1]:
    d2c[i] = next_addr
    next_addr = d1r[i]

outlist = []
for i in list1:
    outlist.append(d1r[i])
    outlist.append(str(i))
    outlist.append(d2c[i])
    print(' '.join(outlist))
    outlist = []

