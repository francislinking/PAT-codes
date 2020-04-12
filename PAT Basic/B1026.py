c1, c2 = map(int,input().split())
CLK_TCK = 100
interval = round((c2-c1)/CLK_TCK)
hour = interval//3600
mint = interval//60%60
secs = interval%60


print('{:02}:{:02}:{:02}'.format(hour,mint,secs))