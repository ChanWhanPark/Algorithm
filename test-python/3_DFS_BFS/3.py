def dfs(graph, v, visited):
    visited[v] = True # 현재 노드를 방문 처리함
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    # 노드와 연결된 다른 노드를 재귀적으로 방문


graph = [
    [], [2, 3, 8], [1, 7], [1, 4, 5],
    [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]
] # 2차원 리스트에서 m행이 어느 열에 연결되어 있는지를 파악할 수 있다.

visited = [False] * 9 # 각 노드는 방문하지 않은 상태임

dfs(graph, 1, visited)

# 스택을 사용함