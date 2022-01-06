## 11403. 경로 찾기 (01.06)
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for row in graph:
    for col in row:
        print(col, end=" ")
    print()