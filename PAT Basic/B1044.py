N = int(input())
unit = ['tret','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec']
dec = ['#','tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou']

for i in range(N):
    line = input()
    try:
        num = int(line)
        a,b = divmod(num,13)
        if a != 0 and b !=0:
            print(dec[a],end=' ')
            print(unit[b])
        elif a == 0:
            print(unit[b])
        elif b == 0:
            print(dec[a])
            
    except:
        line = line.split()
        result = 0
        for x in line:
            if x in unit:
                result += unit.index(x)
            if x in dec:
                result += 13*dec.index(x)
        print(result)
