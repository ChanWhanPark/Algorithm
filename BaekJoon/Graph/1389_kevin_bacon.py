## 1389. 케빈 베이컨의 6단계 법칙 (01.05)
from collections import deque

def bfs(num, n):
    bacon = [0] * (n+1)
    visited = [num]
    queue = deque()
    queue.append(num)

    while queue:
        k = queue.popleft()
        for i in graph[k]:
            # 플로이드-워셜 알고리즘
            if i not in visited:
                bacon[i] = bacon[k] + 1
                visited.append(i)
                queue.append(i)

    return sum(bacon)

n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

kb = []
for i in range(1, n+1):
    kb.append(bfs(i, n))

print(kb.index(min(kb)) + 1)