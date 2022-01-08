## 1388. 바닥 장식 (01.08) S4
n, m = map(int, input().split())
graph = [input() for _ in range(n)]
count = 0

for i in range(n):
    j = 0
    while j < m:
        if graph[i][j] == '|':
            j += 1
        else:
            count += 1
            while j < m and graph[i][j] == '-':
                j += 1

for j in range(m):
    i = 0
    while i < n:
        if graph[i][j] == '-':
            i += 1
        else:
            count += 1
            while i < n and graph[i][j] == '|':
                i += 1

print(count)