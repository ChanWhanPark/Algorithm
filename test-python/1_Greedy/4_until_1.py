# 1이 될 때까지(08.24)
# 2018 E 기업 알고리즘 대회

n, k = map(int, input().split())
count = 0

while True:
    if n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1

    if n == 1:
        break

print(count)

