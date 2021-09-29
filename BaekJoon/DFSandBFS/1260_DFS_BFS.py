## 1260. DFS와 BFS (09.29)
def DFS(v):
    visited_DFS[v] = 1
    print(v, end = " ")
    for i in range(1, n+1):
        if visited_DFS[i] == 0 and graph[v][i] == 1:
            DFS(i)

def BFS(v):
    queue.append(v)
    visited_BFS[v] = 1
    while queue:
        v = queue.pop(0)
        print(v, end=" ")
        for i in range(1, n+1):
            if visited_BFS[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited_BFS[i] = 1

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1

visited_DFS = [0] * (n+1)
visited_BFS = [0] * (n+1)
queue = []

DFS(v)
print()
BFS(v)
