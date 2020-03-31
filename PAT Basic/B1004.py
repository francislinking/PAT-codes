N = int(input())

studentList = []
numberList = []
gradeList = []
for i in range(N):
    student, number, grade = input().split(' ')
    studentList.append(student)
    numberList.append(number)
    gradeList.append(int(grade))

maxIndex = gradeList.index(max(gradeList))
minIndex = gradeList.index(min(gradeList))

print(studentList[maxIndex],numberList[maxIndex])
print(studentList[minIndex],numberList[minIndex])