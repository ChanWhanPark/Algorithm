## 5105. 미로의 거리(09.11)

T = int(input())
answer = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(start_x, start_y):
    global result
    queue.append((start_x, start_y))
    visited.append((start_x, start_y))
    while queue:
        start_x, start_y = queue.pop(0)
        for i in range(4):
            new_x = start_x + dx[i]
            new_y = start_y + dy[i]
            if (0 <= new_x < n and 0 <= new_y < n and (maze[new_x][new_y] == 0 or maze[new_x][new_y] == 3)) and (new_x, new_y) not in visited:
                queue.append((new_x, new_y))
                visited.append((new_x, new_y))
                distance[new_x][new_y] = distance[start_x][start_y] + 1
                if maze[new_x][new_y] == 3:
                    result = distance[new_x][new_y] - 1
                    return

for test_case in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start_x, start_y = i, j

    queue = []
    visited = []
    distance = [[0] * n for _ in range(n)]
    result = 0
    bfs(start_x, start_y)
    answer.append(result)




for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))