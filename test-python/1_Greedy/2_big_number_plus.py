## 큰 수의 법칙(08.24)
## 2019 국가 교육기관 코딩 테스트
## 풀이 업그레이드

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

# 가장 큰 수가 더해지는 횟수
count = int(m / (k+1)) * k # 수열 반복
count += m % (k+1) # 나눠떨어지지 않는 경우

result = 0
result += count * first # 가장 큰 수 더하기
result += (m-count) * second # 두번째로 큰 수 더하기

print(result)