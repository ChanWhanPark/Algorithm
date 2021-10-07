## 15649. N과 M (10.07)

from itertools import permutations

n, m = map(int, input().split())
num_list = [i for i in range(1, n+1)]
per = list(permutations(num_list, m))

for p in per:
    print(' '.join(map(str, p)))