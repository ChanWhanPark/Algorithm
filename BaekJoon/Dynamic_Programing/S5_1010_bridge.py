## 1010. 다리 놓기 (01.07) S5
t = int(input())
dp = [[0] * 30 for _ in range(30)]

for i in range(30):
    for j in range(30):
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1] # 규칙

for i in range(t):
    start, end = map(int, input().split())
    print(dp[start][end])