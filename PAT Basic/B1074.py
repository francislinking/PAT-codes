d = input()
a = input()
b = input()
L = max(len(d),len(a),len(b))
a = a.zfill(L)
b = b.zfill(L)

a = list(map(int,a))
b = list(map(int,b))
d = list(map(int,d))

ans = [0]*L
cin = 0

for i in range(L)[::-1]:
    mod = 10 if d[i] == 0 else d[i]
    s = a[i] + b[i] + cin
    cin, ans[i] = divmod(s,mod)

result = ''.join(map(str,ans))

if cin != 0:
    result = str(cin) + result
    print(result)
else:
    result = result.lstrip('0')
    if result:
        print(result)
    else:
        print(0)