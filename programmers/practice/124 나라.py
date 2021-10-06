## 124 나라의 숫자 (10.06)
def solution(n):
    answer = []
    i = 0
    while n > 0:
        d = 3 ** i
        while (n - d) % 3 ** (i + 1) != 0:
            d += 3 ** i
        answer.append(d // 3 ** i)
        n -= d
        i += 1

    return ''.join(map(str, [4 if i == 3 else i for i in answer][::-1]))

print(solution(10))