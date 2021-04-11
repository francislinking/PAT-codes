N = int(input())

# studentList = []
# numberList = []
# gradeList = []
# for i in range(N):
#     student, number, grade = input().split(' ')
#     studentList.append(student)
#     numberList.append(number)
#     gradeList.append(int(grade))

# maxIndex = gradeList.index(max(gradeList))
# minIndex = gradeList.index(min(gradeList))

# print(studentList[maxIndex],numberList[maxIndex])
# print(studentList[minIndex],numberList[minIndex])

nlist = []
for i in range(N):
    student, number, grade = input().split(' ')
    nlist.append((student,number, grade))


nlist.sort(key = lambda x : int(x[2]),reverse=True)
h = nlist[0]
l = nlist[-1]

print(h[0],h[1])
print(l[0],l[1])