## 1463. 1로 만들기 (10.07, 01.07) S3
n = int(input())
dp = [0] * ((10**6)+1)

for i in range(2, n+1):
    # 3. 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    # 2. 2로 나눠 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])
    # 1. 3으로 나눠 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i//3] + 1, dp[i])

print(dp[n])