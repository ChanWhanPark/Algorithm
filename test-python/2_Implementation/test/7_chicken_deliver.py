## 치킨 배달(08.30)
# 삼성전자 SW 역량테스트

from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

# 모든 치킨집 중 m개의 치킨집을 뽑음
candidates = list(combinations(chicken, m))

# 치킨 거리의 합
def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp

    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)