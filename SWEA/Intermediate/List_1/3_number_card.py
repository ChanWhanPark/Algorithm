## 4834. 숫자 카드 (09.07)
T = int(input())
answer = []
for test_case in range(1, T + 1):
    n = int(input())
    data = input()
    card = [0] * 101
    for i in range(n):
        card[int(data[i])] += 1

    max_value = 0
    for i in range(len(card)):
        if max_value <= card[i]:
            max_value = card[i]
            max_index = i

    answer.append((max_index, max_value))




for test_case in range(T):
    print("#" + str(test_case + 1) + " " + str(answer[test_case][0]) + " " + str(answer[test_case][1]))