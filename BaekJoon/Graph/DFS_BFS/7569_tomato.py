## 7569. 토마토 (01.06) S1
import sys
from collections import deque
m, n, h = map(int, input().split())
tomato = []
queue = deque([])

for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if temp[j][k] == 1:
                queue.append([i, j, k])

    tomato.append(temp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while queue:
    x, y, z = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and tomato[nx][ny][nz] == 0:
            queue.append([nx, ny, nz])
            tomato[nx][ny][nz] = tomato[x][y][z] + 1

day = 0
for i in tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))

print(day-1)

