## 4871. 그래프 경로 (09.09)
T = int(input())
answer = []

def dfs(graph, start, end):
    stack = []
    visited = [0] * (v+1)
    stack.append(start)
    while stack:
        current_node = stack.pop()
        visited[current_node] = True
        for w in graph[current_node]:
            if w not in visited:
                stack.append(w)
    return visited[end]

for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    graph = [[] * (v+1) for _ in range(v+1)]
    for _ in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)
    s, g = map(int, input().split())
    if dfs(graph, s, g):
        answer.append(1)
    else:
        answer.append(0)


for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))