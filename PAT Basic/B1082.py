def getr(x,y):
    x = int(x)
    y = int(y)
    return x**2 + y**2

N = int(input())

minr = 100*100
minname = ''
maxr = -1
maxname = ''

for i in range(N):
    name,x,y = input().split()
    thisr = getr(x,y)
    if  thisr > maxr:
        maxr = thisr
        maxname = name
    
    if thisr < minr:
        minr = thisr
        minname = name

print(minname,maxname)
