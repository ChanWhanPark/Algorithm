## 모의고사 (10.04)
def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a_count = 0
    b_count = 0
    c_count = 0

    for i in range(len(answers)):
        if a[i%5] == answers[i]:
            a_count += 1
        if b[i%8] == answers[i]:
            b_count += 1
        if c[i%10] == answers[i]:
            c_count += 1

    if a_count == b_count == c_count:
        return [1, 2, 3]

    if a_count == b_count and a_count > c_count:
        return [1, 2]
    elif b_count == c_count and b_count > a_count:
        return [2, 3]
    elif c_count == a_count and c_count > b_count:
        return [1, 3]
    else:
        if a_count > b_count and a_count > c_count:
            return [1]
        elif b_count > a_count and b_count > c_count:
            return [2]
        elif c_count > a_count and c_count > b_count:
            return [3]

answers = list(map(int, input().split()))
print(solution(answers))