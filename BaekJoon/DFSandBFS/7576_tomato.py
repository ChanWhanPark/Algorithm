## 7576. 토마토 (10.08)
from collections import deque

n, m = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(m)]
queue = deque()
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            queue.append([i, j])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and tomato[nx][ny] == 0:
            tomato[nx][ny] = tomato[x][y] + 1
            queue.append([nx, ny])

ans = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))
print(ans-1)

