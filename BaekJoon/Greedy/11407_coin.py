## 11407. 동전(10.12)
n, k = map(int, input().split())
money = []
count = 0
for _ in range(n):
    money.append(int(input()))

money.sort(reverse=True)
for m in money:
    if k // m < 1:
        continue
    else:
        count += (k // m)
        k %= m

    if k == 0:
        break

print(count)