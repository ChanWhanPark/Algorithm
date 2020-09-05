n = int(input("공간 입력: "))
x, y = 1, 1
plan = input().split()

# 이동 방향
move = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for p in plan:
    for i in range(len(move)):
        if p == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)