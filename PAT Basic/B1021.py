N = input()
d = {}
for ch in N:
    d[ch] = d.get(ch,0) + 1

result = sorted(d.items(),key= lambda kv:kv[0])

for k,v in result:
    print('{}:{}'.format(k,v))