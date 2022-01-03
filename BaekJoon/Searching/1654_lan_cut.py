## 1654. 랜선 자르기 (01.03)
k, n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))

start, end = 1, max(lan)
while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in lan:
        count += i // mid

    if count >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)