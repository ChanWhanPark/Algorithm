## 11726. 2xn 타일링 (10.08 01.07) S3

n = int(input())
dp = [0] * 1001

dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)