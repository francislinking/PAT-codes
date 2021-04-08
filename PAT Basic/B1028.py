N = int(input())
maxbirth = '1814/09/06'
minbirth = '2014/09/06'
maxname = ''
minname = ''

count = 0
for i in range(N):
    name,birthday = input().split()
    if '1814/09/06' <= birthday <= '2014/09/06':
        count = count + 1
        if birthday >= maxbirth:
            maxname = name
            maxbirth = birthday
        if birthday <= minbirth:
            minname = name
            minbirth = birthday


if count:
    print(count,minname,maxname)
else:
    print(count)
