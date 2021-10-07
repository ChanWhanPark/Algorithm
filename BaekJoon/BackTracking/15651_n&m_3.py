## 15651. n과 m 3 (10.07)

from itertools import product

n, m = map(int, input().split())
num_list = [i for i in range(1, n+1)]
per = list(product(num_list, repeat = m))

for p in per:
    print(' '.join(map(str, p)))