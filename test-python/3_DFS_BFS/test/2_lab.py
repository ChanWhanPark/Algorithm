## 연구소(08.30)
# 삼성전자 SW 역량테스트

n, m = map(int, input().split())
data = []
area = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 바이러스 전파
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if area[nx][ny] == 0:
                area[nx][ny] = 2
                virus(nx, ny) # 재귀적으로 수행

# 안전 영역 크기 계산
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if area[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)를 통한 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치되었을 때
    if count == 3:
        for i in range(n):
            for j in range(m):
                area[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if area[i][j] == 2: # 바이러스인 경우
                    virus(i, j)

        result = max(result, get_score())
        return
    else:
        # 빈 공간에 울타리 설치
        for i in range(n):
            for j in range(m):
                if data[i][j] == 0:
                    data[i][j] = 1
                    count += 1
                    dfs(count)
                    count -= 1
                    data[i][j] = 0


dfs(0)
print(result)