list1=input().upper()
list2=input().upper()
diffSet=set(list1)-set(list2)
for char in list1:
    if char in diffSet:
        diffSet.remove(char)
        print(char,end='')
