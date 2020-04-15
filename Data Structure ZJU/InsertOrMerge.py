# https://github.com/QSCTech-Sange/PAT-in-Python/blob/master/1089-Insert-or-Merge.md
num = int(input())
original = list(map(int, input().split()))
part_sorted = list(map(int, input().split()))
for i in range(1,len(part_sorted)):             # 找第一个不按照从小到大排序的数
    if part_sorted[i] < part_sorted[i - 1]:
        index = i
        break
if original[index:] == part_sorted[index:]:		# 插入排序
    print("Insertion Sort")
    part_sorted = sorted(part_sorted[:index + 1]) + part_sorted[index + 1:]
    print(" ".join(list(map(str, part_sorted))))
else:											# 归并排序
    print("Merge Sort")
    merge_level = 2
    while all([part_sorted[i:i + merge_level] == sorted(part_sorted[i:i + merge_level]) for i in
               range(0, len(part_sorted), merge_level)]):
        merge_level *= 2
    ans = []
    for i in range(0, len(part_sorted), merge_level):
        ans += sorted(part_sorted[i:i + merge_level])
    print(" ".join(list(map(str, ans))))