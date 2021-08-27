## 뱀(08.27)
# 삼성전자 SW 역량테스트

n = int(input()) # 전체 보드 크기
k = int(input()) # 사과의 갯수
map_info = [[0] * (n+1) for _ in range(n+1)]
direction_info = []

for _ in range(k):
    a, b = map(int, input().split())
    map_info[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    direction_info.append((int(x), c))

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 시작 위치
    map_info[x][y] = 2 # 머리 위치
    direction = 0 # 처음은 동쪽을 바라봄
    time = 0
    index = 0 # 회전 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and map_info[nx][ny] != 2: # 범위 내에서
            # 사과가 없으면 꼬리 제거
            if map_info[nx][ny] == 0:
                map_info[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0) # 처음 원소를 가져감
                map_info[px][py] = 0

            if map_info[nx][ny] == 1:
                map_info[nx][ny] = 2
                q.append((nx, ny))

        else:
            time += 1
            break

        x, y = nx, ny # 좌표 갱신
        time += 1

        if index < l and time == direction_info[index][0]: # 회전할 시간인 경우
            direction = turn(direction, direction_info[index][1])
            index += 1

    return time

result = simulate()
print(result)