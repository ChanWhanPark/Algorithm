## 4828 min,max (09.06)

T = int(input())
answer = []
for test_case in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()
    answer.append(int(data[-1] - data[0]))

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))