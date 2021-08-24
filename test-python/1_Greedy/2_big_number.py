## 큰 수의 법칙(08.24)
## 2019 국가 교육기관 코딩 테스트

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

result = 0
count = 0
while True:
    for i in range(k):
        if count == m:
            break
        result += first
        count += 1

    if count == m:
        break
    result += second
    count += 1


print(result)
