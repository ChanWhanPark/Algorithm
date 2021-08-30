## 경쟁적 전염(08.30)
from collections import deque

n, k = map(int, input().split())

area = []
virus = []

for i in range(n):
    area.append(list(map(int, input().split())))
    for j in range(n):
        if area[i][j] != 0:
            # 바이러스 종류, 시간, x, y 좌표 삽입
            virus.append((area[i][j], 0, i, j))

virus.sort()
q = deque(virus)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while q:
    v, s, x, y = q.popleft()
    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if area[nx][ny] == 0:
                area[nx][ny] = v
                q.append((v, s+1, nx, ny))

print(area[target_x-1][target_y-1])