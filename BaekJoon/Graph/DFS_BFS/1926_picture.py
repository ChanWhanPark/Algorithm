## 1926. 그림 (10.14)
def BFS(x, y):
    queue = []
    queue.append([x, y])
    area = 0
    if visited[x][y] == 1:
        return
    else:
        visited[x][y] = 1
        while queue:
            xx, yy = queue.pop()
            for i in range(4):
                nx = xx + dx[i]
                ny = yy + dy[i]
                if 0 <= nx < n and 0 <= ny < m and paper[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                    area += 1
        if area != 0:
            picture.append(area)

    return

n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
picture = []

for i in range(n):
    for j in range(m):
        BFS(i, j)

print(len(picture))
if len(picture) == 0:
    print(0)
else:
    print(max(picture))