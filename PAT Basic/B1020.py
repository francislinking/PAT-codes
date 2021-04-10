from decimal import *
N, D = [int(x) for x in input().split()]
unit_price = [0]*N

reserve = [Decimal(x) for x in input().split()]
total_price = [Decimal(x) for x in input().split()]

for i in range(N):
    unit_price[i] = total_price[i]/reserve[i]

tlist = list(zip(unit_price,reserve,total_price))

tlist.sort(key=lambda x:-x[0])

result = 0
for item in tlist:
    if D >= item[1]:
        D = D - item[1]
        result = result + item[2]
    else:
        result = result + D*item[0]
        break

print('{:.2f}'.format(result))