N = int(input())
line = input().split()

count = 0
isum = 0
for ch in line:
    try:
        num = float(ch)
    except:
        print('ERROR: {} is not a legal number'.format(ch))
        continue

    numf = round(num,2)

    if num == numf and -1000 <= num <= 1000:
        count += 1
        isum += num
    else:
        print('ERROR: {} is not a legal number'.format(ch))

if count == 1:
    print('The average of 1 number is {:.2f}'.format(isum))
elif count > 1:
    print('The average of {} numbers is {:.2f}'.format(count,isum/count))
else:
    print('The average of 0 numbers is Undefined')


     
