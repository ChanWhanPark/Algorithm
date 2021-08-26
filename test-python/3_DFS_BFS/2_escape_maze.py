## 미로 탈출(08.26)
from collections import deque

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

count = 0

dx = [-1, 1, 0, 0] # 북, 남, 서, 동
dy = [0, 0, -1, 1] # 북, 남, 서, 동

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            elif maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[n-1][m-1]

