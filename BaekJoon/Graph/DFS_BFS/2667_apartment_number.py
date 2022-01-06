## 2667. 단지 번호 붙이기 (09.29)
def DFS(x, y):
    global count
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False

n = int(input())
graph = []
cnt = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0
result = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            cnt.append(count)
            result += 1
            count = 0
cnt.sort()
print(result)
for i in range(result):
    print(cnt[i])