n, m = map(int, input().split())

# 그래프 정보 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#DFS로 특정 노드 방문 후 연결된 모든 노드들 방문 처리
def dfs(x, y):
    # 주어진 범위를 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        # 좌, 우, 상, 하 재귀적 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)