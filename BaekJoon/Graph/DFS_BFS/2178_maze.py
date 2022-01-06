## 2178. 미로 탐색 (09.30)
def BFS():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue = [[0, 0]]
    while queue:
        x, y = queue[0][0], queue[0][1]
        queue.pop(0)
        if x == n-1 and y == m-1:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append([nx, ny])

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

BFS()

print(maze[n-1][m-1])