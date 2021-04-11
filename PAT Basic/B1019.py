n = sorted([x for x in input().rjust(4,'0')])
a = int(''.join(n[::-1]))
b = int(''.join(n))
if a == b:
    print('{:0>4d} - {:0>4d} = 0000'.format(a,b))
else:
    while(1):
        c = a - b
        print('{:0>4d} - {:0>4d} = {:0>4d}'.format(a,b,c))
        if c == 6174:
            break
        else:
            n = sorted([x for x in str(c).rjust(4,'0')])
            a = int(''.join(n[::-1]))
            b = int(''.join(n))