## 4835. 구간합(09.07)
T = int(input())
answer = []
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    sum_min = 1e9
    sum_max = -1e9
    for k in range(0, len(data)-m+1):
        temp = 0
        for i in range(k, m+k):
            temp += data[i]
        if temp <= sum_min:
            sum_min = temp
        if temp >= sum_max:
            sum_max = temp

    result = sum_max - sum_min

    answer.append(result)

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))