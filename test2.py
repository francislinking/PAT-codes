n,k = [int(x) for x in input().split()]

user_array = [None]*(n+1)
d = {}
for i in range(1,n+1):
    user_array[i] = int(input())
    d[i] = (user_array[i],1)

while(k):
    list = sorted(d.items(),key= lambda k:(k[1][0],k[0]))
    key = list[0][0]
    times = d[key][1] + 1
    newval = user_array[key]*times
    d[key] = (newval,times)
    print(key)


    k -=1 