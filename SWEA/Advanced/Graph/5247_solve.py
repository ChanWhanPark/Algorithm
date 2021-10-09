## 5247. 계산 (10.08)
from collections import deque
def BFS():
    global n, m, result, test_case
    while queue:
        num, cnt = queue.popleft()
        if num == m:
            result = cnt
            return

        for i in range(4):
            num2 = 0
            if i == 0:
                num2 = num + 1
                if 0 < num2 < 1000000 and num_list[num2] != test_case:
                    queue.append((num2, cnt + 1))
                    num_list[num2] = test_case
            elif i == 1:
                num2 = num - 1
                if 0 < num2 < 1000000 and num_list[num2] != test_case:
                    queue.append((num2, cnt + 1))
                    num_list[num2] = test_case
            elif i == 2:
                num2 = num * 2
                if 0 < num2 < 1000000 and num_list[num2] != test_case:
                    queue.append((num2, cnt + 1))
                    num_list[num2] = test_case
            elif i == 3:
                num2 = num - 10
                if 0 < num2 < 1000000 and num_list[num2] != test_case:
                    queue.append((num2, cnt + 1))
                    num_list[num2] = test_case

T = int(input())
num_list = [0] * 1000001
answer = []
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    queue = deque()
    queue.append((n, 0))
    num_list[n] = test_case
    result = 0
    BFS()
    answer.append(result)

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))