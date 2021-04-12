line = input()

d = {}
for ch in line.lower():
    if ch.isalpha():
        d[ch] = d.get(ch,0) + 1

result = sorted(d.items(),key= lambda k : (-k[1],k[0]))

print(result[0][0],result[0][1])