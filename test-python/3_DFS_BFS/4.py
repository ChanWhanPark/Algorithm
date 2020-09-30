from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [], [2, 3, 8], [1, 7], [1, 4, 5],
    [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]
] # 2차원 리스트에서 m행이 어느 열에 연결되어 있는지를 파악할 수 있다.

visited = [False] * 9

bfs(graph, 1, visited)