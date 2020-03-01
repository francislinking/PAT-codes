N, ref = map(int, input().split())

records = []

for i in range(N):
    s_id, name, score = input().split()
    records.append([s_id, name, score])

records.sort(key=lambda x: (x[ref - 1],x[0]))
for i in records:
    print(" ".join(i))