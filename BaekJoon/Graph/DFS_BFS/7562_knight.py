## 7562. 나이트의 이동
def BFS():
    dx = [-1, -2, -2, -1, 1, 2, 1, 2]
    dy = [2, 1, -1, -2, -2, -1, 2, 1]
    queue = []
    queue.append([start_x, start_y])
    while queue:
        x, y = queue.pop(0)
        if x == end_x and y == end_y:
            print(chess[x][y])
            break
        for idx in range(8):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < i and 0 <= ny < i and not chess[nx][ny]:
                chess[nx][ny] = chess[x][y] + 1
                queue.append([nx, ny])

T = int(input())
answer = []
for test_case in range(1, T + 1):
    i = int(input())
    chess = [[0] * (i+1) for _ in range(i+1)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    BFS()