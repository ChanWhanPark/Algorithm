## 개미 전사 (09.06)

n = int(input())
data = list(map(int, input().split()))

d = [0] * 100

# Dynamic Programming
d[0] = data[0]
d[1] = max(data[0], data[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + data[i])

print(d[n-1])