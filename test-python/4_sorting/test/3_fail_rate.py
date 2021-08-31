## 실패율 (08.31)
# 2019 카카오 신입 공채 1차

def solution(n, stages):
    rate = []
    length = len(stages)
    for i in range(1, n+1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        rate.append((i, fail))
        length -= count

    rate = sorted(rate, key=lambda t:t[1], reverse=True)
    rate = [i[0] for i in rate]
    return rate

n = int(input())
stages = list(map(int, input().split()))
result = solution(n, stages)
print(result)