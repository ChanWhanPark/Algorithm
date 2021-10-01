## 1697. 숨바꼭질 (10.01)
def BFS():
    queue = []
    queue.append(n)
    while queue:
        x = queue.pop(0)
        if x == k:
            print(graph[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < len(graph) and not graph[nx]:
                graph[nx] = graph[x] + 1
                queue.append(nx)



n, k = map(int, input().split())
graph = [0] * 100001
BFS()