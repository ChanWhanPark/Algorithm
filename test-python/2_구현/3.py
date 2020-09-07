#맵 크기 입력
n, m = map(int, input().split())

# 방문 위치 저장 위한 맵 생성
d = [[0] * m for _ in range(n)] # n*m 행렬을 모두 0으로 채움
x, y, direction = map(int, input().split()) # 캐릭터의 현위치, 방향
d[x][y] = 1 # 방문 처리

# 전체 맵 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
# 방향 정의(북 동 남 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0: # 정면에 가보지 않은 칸이 존재하는 경우
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else: # 정면에 가보지 않은 칸이 없거나 바다인 경우
        turn_time += 1
    if turn_time == 4: # 갈 곳이 없는 경우
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0: # 뒤로 갈 수 있다면
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)