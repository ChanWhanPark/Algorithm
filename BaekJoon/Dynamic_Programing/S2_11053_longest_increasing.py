## 11053. 가장 긴 증가하는 부분 수열 (01.08) S2
n = int(input())
num_list = list(map(int, input().split()))
dp = [0 for i in range(len(num_list))]
'''
last_max = num_list[0]
for i in range(1, len(num_list)):
    if num_list[i] > num_list[i-1] and num_list[i] > last_max:
        last_max = num_list[i]
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]
'''
for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))