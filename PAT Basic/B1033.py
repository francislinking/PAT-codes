errorkey = list(input())
line = list(input())

# print(errorkey)
# print(line)

upper = 0
if '+' in errorkey:
    upper = 1

for ch in line:
    if ch.isalpha():
        if ch.upper() not in errorkey:
            if upper == 0:
                print(ch,end='')
            elif ch.islower():
                print(ch,end='')
    else:
        if ch not in errorkey:
            print(ch,end='')