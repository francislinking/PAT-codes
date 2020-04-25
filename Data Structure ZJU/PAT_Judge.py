# https://github.com/QSCTech-Sange/PAT-in-Python/blob/master/1075-PAT-Judge.md
from collections import defaultdict

num_users, num_pro, num_sub = list(map(int, input().split()))
full = list(map(int, input().split()))
scores = defaultdict(lambda: [-2 for _ in range(num_pro)])
for _ in range(num_sub):
    id, pro, score = input().split()
    scores[id][int(pro) - 1] = max(scores[id][int(pro) - 1], int(score))

total_score = defaultdict(int)
for id in scores.keys():
    total_score[id] = sum([i for i in scores[id] if i != -2 and i != -1])

ids = sorted(scores.keys(),
             key=lambda x: (-total_score[x], -len([i for i in range(num_pro) if full[i] == scores[x][i]]), int(x)))

rank = 0
for i, id in enumerate(ids):
    if set(scores[id]).issubset({-1, -2}):
        break
    if rank == 0 or total_score[id] != total_score[ids[i - 1]]:
        rank = i + 1
    print(rank, id, total_score[id], end=" ")
    ans = " ".join(list(map(str, scores[id]))).replace("-2", "-").replace("-1", "0")
    print(ans)