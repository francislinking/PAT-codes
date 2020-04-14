c1, c2 = map(int,input().split())
CLK_TCK = 100
interval = round((c2-c1)/CLK_TCK)
hour = interval//3600
minute = interval//60%60
second = interval%60

print('{:02}:{:02}:{:02}'.format(hour,minute,second))