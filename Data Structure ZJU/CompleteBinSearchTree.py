# https://www.liuchuo.net/archives/2161
def inOrder(root):
    global input_num,count
    global levelOrederList
    if root < input_num:
        inOrder(root*2 +1)
        levelOrederList[root] = input_list[count]
        count +=1
        inOrder(root*2 +2)



input_num = int(input())
input_list = list(map(int,input().split()))

levelOrederList = [None]*input_num
count = 0

input_list.sort()

inOrder(0)

print(' '.join(list(map(str,levelOrederList))))