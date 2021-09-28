## 4869. 종이 붙이기 (09.08)
T = int(input())
answer = []
for test_case in range(1, T + 1):
    area = int(input())

    d = [0] * 300
    d[1] = 1 # 10을 채울 수 있는 가지수
    d[2] = 3 # 20을 채울 수 있는 가지수
    for i in range(3, (area//10)+1):
        d[i] = d[i-1] + (2 * d[i-2])

    answer.append(d[area//10])

for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case]))