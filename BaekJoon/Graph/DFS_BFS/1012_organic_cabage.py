## 1012. 유기농 배추 (09.30)
def BFS(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    queue = [[x, y]]

    while queue:
        a, b = queue[0][0], queue[0][1]
        queue.pop(0)
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])

T = int(input())
answer = []
for test_case in range(1, T + 1):
    m, n, k = map(int, input().split())
    count = 0
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                BFS(i, j)
                graph[i][j] = 0
                count += 1

    print(count)

