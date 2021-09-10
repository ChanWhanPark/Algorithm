## 4881. 배열 최소 합(09.10)
T = int(input())
answer = []

def find_min(row):
    global my_sum, my_min
    # 합이 최솟값을 넘으면 버림
    if my_sum > my_min:
        return
    # 범위를 벗어나면 최솟값 갱신
    if row == n:
        if my_sum < my_min:
            my_min = my_sum
            return

    for col in range(n):
        if not visited[col]:
            visited[col] = True
            my_sum += data[row][col]
            find_min(row+1)
            my_sum -= data[row][col]
            visited[col] = False

for test_case in range(1, T + 1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    my_sum, my_min = 0, n*9
    find_min(0)
    answer.append(my_min)


for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))