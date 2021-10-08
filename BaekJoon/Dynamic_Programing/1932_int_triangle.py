## 1932. 정수 삼각형(10.08)
n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            up_left = 0
        else:
            up_left = triangle[i-1][j-1]
        if j == i:
            up = 0
        else:
            up = triangle[i-1][j]

        triangle[i][j] += max(up_left, up)

print(max(triangle[n-1]))