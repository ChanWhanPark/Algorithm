## 2206. 벽 부수고 이동하기 (10.08)
from collections import deque
def bfs(start_x, start_y, is_crash):
    queue = deque()
    queue.append((start_x, start_y, is_crash))
    visited[start_x][start_y][is_crash] = 1

    while queue:
        cur_x, cur_y, is_crash = queue.popleft()
        if cur_x == n - 1 and cur_y == m - 1:
            return visited[cur_x][cur_y][is_crash]
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if next_x <= -1 or next_x >= n or next_y <= -1 or next_y >= m:
                continue
            if graph[next_x][next_y] == 0 and visited[next_x][next_y][is_crash] == 0:
                queue.append((next_x, next_y, is_crash))
                visited[next_x][next_y][is_crash] = visited[cur_x][cur_y][is_crash] + 1
            if graph[next_x][next_y] == 1 and is_crash == 0:
                queue.append((next_x, next_y, is_crash + 1))
                visited[next_x][next_y][is_crash + 1] = visited[cur_x][cur_y][is_crash] + 1

    return -1
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
print(bfs(0, 0, 0))



