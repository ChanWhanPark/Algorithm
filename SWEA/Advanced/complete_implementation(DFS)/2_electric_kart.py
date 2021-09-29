## 5189. 전자 카트 (09.29)
def DFS(node):
    global min_val, sum_val

    if sum_val < min_val:
        visited[node] = True

        if False not in visited: # 모든 곳을 방문하면 사무실로 돌아옴
            sum_val += data[node][0]
            if sum_val < min_val: # 최솟값이면 갱신
                min_val = sum_val
            sum_val -= data[node][0] # 재귀적으로 불러왔으므로 원상태로 복원
        else:
            for next in range(n):
                if visited[next] == False:
                    sum_val += data[node][next]
                    DFS(next)
                    sum_val -= data[node][next]

        visited[node] = False

T = int(input())
answer = []
for test_case in range(1, T + 1):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))

    visited = [False] * n
    min_val = 1e9
    sum_val = 0
    DFS(0)
    answer.append(min_val)

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))