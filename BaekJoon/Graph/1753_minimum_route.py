import heapq
def dijkstra(k):
    dp[k] = 0
    heapq.heappush(heap, [0, k])
    while heap:
        w, n = heapq.heappop(heap)
        for n_n, weight in graph[n]:
            n_w = weight + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heapq.heappush(heap, [n_w, n_n])


v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
inf = 1e9
dp = [inf] * (v+1)
heap = []

for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
dijkstra(k)

for i in dp[1:]:
    print(i if i != inf else "INF")