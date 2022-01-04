## 2108. 통계학 (Counter 모듈 사용) (01.03)
import sys
from collections import Counter
n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))

# 1. 산술평균
print(round(sum(array)/n))

# 2. 중앙값
array.sort()
print(array[n//2])

# 3. 최빈값
count_array = Counter(array).most_common()
if len(count_array) > 1 and count_array[0][1] == count_array[1][1]:
    print(count_array[1][0])
else:
    print(count_array[0][0])

# 4. 범위
print(array[-1]-array[0])