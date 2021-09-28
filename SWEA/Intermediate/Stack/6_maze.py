## 4875. 미로 (09.10)

T = int(input())
answer = []

def dfs(x, y):
    global result
    if maze[x][y] == 3:
        result = 1
        return

    visited.append((x, y))
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if (0 <= new_x < n and 0 <= new_y < n and (maze[new_x][new_y] == 0 or maze[new_x][new_y] == 3)) and (new_x, new_y) not in visited:
            dfs(new_x, new_y)

for test_case in range(1, T + 1):
    n = int(input())
    maze = []
    for _ in range(n):
        maze.append(list(map(int, input())))
    visited = []
    result = 0
    # 시작점 찾기
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start_x, start_y = i, j

    dx = [-1, 1, 0, 0]  # 북, 서, 남, 동
    dy = [0, 0, -1, 1]
    dfs(start_x, start_y)
    answer.append(result)


for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))