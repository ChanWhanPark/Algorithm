## 치킨 배달(08.27)_미풀이
# 삼성전자 SW 역량테스트

from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[r][c] == 1:
            house.append((r, c))
        elif data[r][c] == 2:
            chicken.append((r, c))

candidates = list(combinations(chicken, m))
print(candidates)