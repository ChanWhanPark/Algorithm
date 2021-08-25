## 게임 개발(08.25)_미풀이
n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


print(array)
