numList = input()

# print(numList[0])
nSum = 0
for x in numList:
    nSum += int(x)
strSum = str(nSum)
# print(strSum[0])
charList = ['ling','yi','er','san','si', 'wu', 'liu', 'qi', 'ba', 'jiu']

# for x in charList:
#     print(x)

outList = []
for index in map(int,strSum):
    outList.append(charList[index])

print(' '.join(outList))