line1 = input()
line2 = input()
line3 = input()
line4 = input()

L1 = len(line1)
L2 = len(line2)
L3 = len(line3)
L4 = len(line4)

WeekList = ['MON','TUE','WED','THU','FRI','SAT','SUN']

for i in range(0,60):
    if line1[i] == line2[i]:
        if 'A'<=line1[i]<='G':
            day = WeekList[ord(line1[i]) - ord('A')]
            break

for j in range(i+1,60):
    if line1[j] == line2[j]:
        if 'A'<=line1[j]<='N':
            hour = ord(line1[j]) - ord('A') + 10
            break
        elif line1[j].isdecimal():
            hour = line1[j]
            break

for k in range(0,60):
    if line3[k] == line4[k] and line3[k].isalpha() and line4[k].isalpha():
        mint = k
        break

print("{0} {1:0>2}:{2:0>2}".format(day,hour,mint)) 