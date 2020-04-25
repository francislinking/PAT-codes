N = input()
list1 = [int(x) for x in input().split()]
counts = {}

for item in list1:
    counts[item] = counts.get(item,0)+1 

countsList = list(counts.items())
countsList.sort(key=lambda x: x[0])

for item in countsList:
    print('{}:{}'.format(item[0],item[1]))