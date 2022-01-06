## 11659. 구간 합 구하기 4 (01.06) S3
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_add = [0]

for i in range(n):
    num_add.append(num_add[-1]+num_list[i])

for _ in range(m):
    start, end = map(int, input().split())
    if start == 1:
        print(num_add[end])
    else:
        print(num_add[end] - num_add[start-1])