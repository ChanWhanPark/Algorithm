## 15651. n과 m 4 (10.07)

from itertools import combinations_with_replacement

n, m = map(int, input().split())
num_list = [i for i in range(1, n+1)]
per = list(combinations_with_replacement(num_list, m))

for p in per:
    print(' '.join(map(str, p)))