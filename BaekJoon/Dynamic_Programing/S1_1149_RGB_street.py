## 1149. RGB 거리 (01.07) S1
n = int(input())
cost = [[0 for _ in range(3)] for _ in range(n)]

for i in range(n):
    r, g, b = map(int, input().split())
    cost[i][0], cost[i][1], cost[i][2] = r, g, b

for i in range(1, len(cost)):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]

print(min(cost[n-1]))