## 4861. 회문(09.08)

T = int(input())
answer = []
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = []
    result = []
    count = 0
    for _ in range(n):
        arr.append(list(input()))

    ## 가로로 회문이 있는지 검사
    for i in range(n):
        for j in range(n-m+1):
            if arr[i][j:j+m] == arr[i][j:j+m][::-1]:
                result.append(''.join(map(str, arr[i][j:j+m])))

    ## 세로로 회문이 있는지 검사
    for i in range(n-m+1):
        for j in range(n):
            col_list = []
            for k in range(m):
                col_list.append(arr[i+k][j])
            if col_list == col_list[::-1]:
                result.append(''.join(map(str, col_list)))

    answer.append(''.join(map(str, result)))

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))
