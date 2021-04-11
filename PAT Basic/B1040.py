line = input()
count_T = line.count('T')
count_P = 0
mod = 1000000007

result = 0
for ch in line:
    if ch == 'P':
        count_P += 1
    if ch == 'T':
        count_T -= 1
    if ch == 'A':
        temp = ( count_P * count_T ) % mod
        result = (result + temp) %mod

print(result)