line = input()
d = {'P':0,'A':0,'T':0,'e':0,'s':0,'t':0}

for ch in line:
    try:
        d[ch] +=1
    except:
        pass

dset = set(d.keys())
refset = set()
while(d):
    for k,v in d.items():
        if d[k] != 0:
            d[k] -=1
            print(k,end='')
        else:
            refset.update(k)

    if dset == refset:
        break