## 5188. 최소합 (09.29)
def make_min_sum(x_index, y_index):
    global sum_val, sum_result
    if sum_result < sum_val:
        return
    if x_index == n-1 and y_index == n-1:
        sum_result = sum_val
        return
    for i in range(2):
        new_x = x_index + dx[i]
        new_y = y_index + dy[i]
        if 0 <= new_x <= n-1 and 0 <= new_y <= n-1 and (new_x, new_y) not in visited:
            visited.append((new_x, new_y))
            sum_val += data[new_x][new_y]
            make_min_sum(new_x, new_y)
            visited.remove((new_x, new_y)) # 원래대로 돌리기
            sum_val -= data[new_x][new_y]
    return

T = int(input())
answer = []
for test_case in range(1, T + 1):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))

    sum_val = data[0][0]
    sum_result = 1e9

    visited = []

    dx = [1, 0]
    dy = [0, 1]

    make_min_sum(0, 0)
    answer.append(sum_result)

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))