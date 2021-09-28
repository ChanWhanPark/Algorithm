## 5097. 회전 (09.10)
T = int(input())
answer = []
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    queue = []
    queue.append(data)
    for i in range(m):
        queue.pop()
        queue.append(data[(i+1)%n])

    answer.append(queue[0])

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))