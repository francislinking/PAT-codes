N = int(input())

PhoneDict = {}
for i in range(N):
    p1, p2 = map(int,input().split())
    PhoneDict[p1] = PhoneDict.get(p1,0)+1
    PhoneDict[p2] = PhoneDict.get(p2,0)+1

PhoneList = list(PhoneDict.items())

PhoneList.sort(key= lambda x:(x[1],-x[0]),reverse=True)
freq = [x[1] for x in PhoneList]
N = freq.count(freq[0])
if N == 1:
    print(PhoneList[0][0],PhoneList[0][1])
else:
    print(PhoneList[0][0],PhoneList[0][1],N)
