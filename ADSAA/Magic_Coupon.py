#https://qsctech-sange.github.io/1037-Magic-Coupon.html#%E6%80%9D%E8%B7%AF
num_a = int(input())
a = list(map(int, input().split()))

a_pos = sorted([i for i in a if i > 0], reverse=True)
a_neg = sorted([i for i in a if i < 0])

num_b = int(input())
b = list(map(int, input().split()))

b_pos = sorted([i for i in b if i > 0], reverse=True)
b_neg = sorted([i for i in b if i < 0])

print(sum([i * j for i, j in zip(a_pos, b_pos)]) + sum([i * j for i, j in zip(a_neg, b_neg)]))
