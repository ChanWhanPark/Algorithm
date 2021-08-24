## 숫자 카드 게임(08.24)
## 2019 국가 교육기관 코딩 테스트

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    if result < min_value:
        result = min_value

    last_min_value = min_value

print(result)