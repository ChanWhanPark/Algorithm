## BFS 구현 (08.26)
from collections import deque

graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

graph2 = {
    1: [2, 3, 8],
    2: [1, 7],
    3: [1, 4, 5],
    4: [3, 5],
    5: [3, 4],
    6: [7],
    7: [2, 6, 8],
    8: [1, 7]
}

visited = [False] * 100
visited2 = [False] * 100

def bfs_queue(graph, start, visit):
    queue = deque([start])
    visit[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True


bfs_queue(graph, 1, visited)
print(end="\n")
bfs_queue(graph2, 1, visited2)


