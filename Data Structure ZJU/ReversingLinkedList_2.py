d={}

start_addr, L, K = input().split(' ')
L = int(L)
K = int(K)

for i in range(L):
    addr1, data, next_addr = input().split(' ')
    d[addr1] = [data,next_addr]

addr_list = []
count = 0
temp_addr = start_addr 
for i in range(L):
    if temp_addr == '-1':
        break
    else:
        count += 1
        addr_list.append(temp_addr)
        temp_addr = d[temp_addr][1]

res_index = 0
while(res_index + K <= count):
    sub_list = addr_list[res_index:res_index+K]
    addr_list[res_index:res_index+K] = sub_list[::-1]
    res_index += K

for i in range(len(addr_list) - 1):
    print(addr_list[i],d[ addr_list[i] ][0],addr_list[i+1])
print(addr_list[-1],d[ addr_list[-1] ][0],'-1')