https://github.com/QSCTech-Sange/PAT-in-Python/blob/master/1010-Radix.md

def convert(string,radix):
    result = 0
    for char in string:
        if char.isdigit():
            result = result*radix + int(char)
        else:
            result = result*radix + ord(char) - ord('a') +10
    return result


line = input().split()
if line[2] == '1':
    original = line[0]
    target = line[1]
else:
    original = line[1]
    target = line[0]
radix = int(line[3])

original_num = convert(original,radix)

min_radix = chr(max([ord(char) for char in target]))

if min_radix.isdigit():
    min_radix_num = int(min_radix) + 1
else:
    min_radix_num = ord(min_radix) - ord('a') + 10

low = min_radix_num
high = max(min_radix_num,original_num)

while low < high:
    mid = (low+high)//2
    temp = convert(target,mid)
    if temp < original_num:
        low = mid +1
    else:
        high = mid

if convert(target,low) == original_num:
    print(low)
else:
    print("Impossible")
