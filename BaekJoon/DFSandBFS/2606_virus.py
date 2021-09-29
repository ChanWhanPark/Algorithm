## 2606. 바이러스 (09.29)
def virus(n):
    queue = []
    queue.append(n)
    visited[n] = 1
    count = 0
    while queue:
        current = queue.pop(0)
        for i in range(1, computer+1):
            if visited[i] == 0 and network[current][i] == 1:
                queue.append(i)
                count += 1
                visited[i] = 1
    return count


computer = int(input())
node = int(input())
network = [[0] * (computer + 1) for _ in range(computer+1)]

for _ in range(node):
    a, b = map(int, input().split())
    network[a][b] = network[b][a] = 1

visited = [0] * (computer + 1)

result = virus(1)
print(result)