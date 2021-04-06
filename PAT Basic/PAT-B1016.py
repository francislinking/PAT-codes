def P(N,DN):
    PN = 0
    for item in N:
        if DN == item:
            PN = PN*10 + int(DN)

    return PN

A, DA, B, DB  = [x for x in input().split()]

PA = P(A,DA)
PB = P(B,DB)

print(PA+PB)