## 4837. 부분집합(09.07)
T = int(input())
answer = []
for test_case in range(1, T + 1):
    arr = list(range(1, 13))
    n, k = map(int, input().split())

    count = 0
    for i in range(1 << len(arr)): # 부분집합 케이스
        currentSet = []

        for j in range(len(arr)):
            if i & (1 << j):
                currentSet.append(arr[j])

        if len(currentSet) == n and sum(currentSet) == k:
            count += 1

    answer.append(count)

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))