## 15650. n과 m 2 (10.07)

from itertools import combinations

n, m = map(int, input().split())
num_list = [i for i in range(1, n+1)]
per = list(combinations(num_list, m))

for p in per:
    print(' '.join(map(str, p)))