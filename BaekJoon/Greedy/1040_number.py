## 1040. 정수 (10.30)
n, k = map(int, input().split())
len = 0
i = 1

while True:
    if n // (10 ** i) == 0:
        len = i
        break
    else:
        i += 1
