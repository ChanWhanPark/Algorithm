## 2839. 설탕 배달 (01.07) B1
n = int(input())
count = 0

if n % 5 == 0:
    print(n//5)
    exit(0)

while n > 0:
    n -= 3
    count += 1
    if n % 5 == 0:
        count += (n // 5)
        print(count)
        exit(0)

print(-1)