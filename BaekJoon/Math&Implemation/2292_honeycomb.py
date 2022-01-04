## 2292. 벌집 (01.04)
n = int(input())
start = 1
change = start
idx = 0
while True:
    if start == n:
        break
    start += 1
    if start >= (change + 6*idx):
        idx += 1
        change = start

print(idx+1)