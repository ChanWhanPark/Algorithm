## 상하좌우(08.25)

x = 1
y = 1

n = int(input())
move = input().split()
move_list = ['L', 'R', 'U', 'D']

move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]


for m in move:
    for i in range(len(move_list)):
        if m == move_list[i]:
            nx = x + move_x[i]
            ny = y + move_y[i]

    if nx <= 0 or nx > n or ny <= 0 or ny > n:
        continue

    x, y = nx, ny # 좌표를 초기화함

print(x, y)
