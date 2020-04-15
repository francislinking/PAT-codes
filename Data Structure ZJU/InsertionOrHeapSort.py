# 数据读入
n = int(input())
original = [-9999] + list(map(int, input().split()))
half_sorted = [-9999] + list(map(int, input().split()))

# temp找到第一个非从小到大排序的下标
temp = 2
while temp <= n and half_sorted[temp - 1] <= half_sorted[temp]:
    temp += 1

# 如果temp之后两个数组相同，那么这就是插入排序。将半排序后的数组再往后排一位
if original[temp:] == half_sorted[temp:]:
    print("Insertion Sort")
    half_sorted = sorted(half_sorted[:temp + 1]) + half_sorted[temp + 1:]

# 否则，就是堆排
else:
    print("Heap Sort")
    # temp变量从后往前找到第一个比第一项少的数（即还没排的数），根据堆排序的性质，第一项为还未排序的最大值
    temp = n
    while temp > 2 and half_sorted[temp] >= half_sorted[1]:
        temp -= 1
    # 将第一项和temp项交换，这样第一项就是更小的了，temp项的位置就固定了
    half_sorted[1], half_sorted[temp] = half_sorted[temp], half_sorted[1]
    # 现在的第一项要开始下滤，i是j的父亲节点索引,j是i的左孩子
    i, j = 1, 2
    while j <= temp - 1:
        # 判断j要不要变成右孩子，下滤只和更大的那个交换
        if j + 1 <= temp - 1 and half_sorted[j] < half_sorted[j + 1]:
            j = j + 1
        # 交换并更新i和j，相当于下滤
        half_sorted[i], half_sorted[j] = half_sorted[j], half_sorted[i]
        i, j = j, j * 2

# 输出排序好的下一项
print(" ".join(map(str, half_sorted[1:])))