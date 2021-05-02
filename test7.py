class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 
# @param S ListNode类 val表示权值，next指向下一个元素
# @return ListNode类
#

S = ListNode(1)
T = ListNode(2)
U = ListNode(3)
V = ListNode(4)
S.next = T
T.next = U
U.next = V

head = S
temp = S.next

while(head.val < temp.val):
    temp = temp.next if temp.next != None else S
