line = input()
s = 0
for ch in line:
    if ch.isalpha():
        s = s + ord(ch.upper())-ord('A') + 1

s0 = 0
s1 = 0

while s:
    if s % 2 == 0:
        s0 = s0 + 1
    else:
        s1 = s1 + 1

    s = s//2  

print(s0,s1)