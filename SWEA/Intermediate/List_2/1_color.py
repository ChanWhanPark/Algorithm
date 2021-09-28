## 4836 색칠하기(09.07)

T = int(input())
answer = []
for test_case in range(1, T + 1):
    n = int(input())
    area = [[0] * 10 for _ in range(10)]
    pupple = 0
    for i in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for j in range(10):
            for k in range(10):
                if (j >= r1 and j <= r2) and (k >= c1 and k <= c2):
                    area[j][k] += color


    for j in range(10):
        for k in range(10):
            if area[j][k] == 3:
                pupple += 1

    answer.append(pupple)

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))