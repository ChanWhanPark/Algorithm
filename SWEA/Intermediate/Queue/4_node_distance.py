## 5102. 노드의 거리(09.15)
T = int(input())
answer = []

def bfs(s, g):
    global result
    queue.append(s)
    visited[s] = 1

    while queue:
        s = queue.pop(0)
        for next in range(1, v+1):
            if graph[s][next] and not visited[next]:
                queue.append(next)
                visited[next] = 1
                distance[next] = distance[s] + 1
                if next == g:
                    result = distance[next]
                    return

for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    graph = [[0] * (v+1) for _ in range(v+1)]
    for _ in range(e):
        start, end = map(int, input().split())
        graph[start][end] = 1
        graph[end][start] = 1
    s, g = map(int, input().split())

    result = 0
    queue = []
    visited = [0] * (v+1)
    distance = [0] * (v+1)
    bfs(s, g)
    answer.append(result)

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))