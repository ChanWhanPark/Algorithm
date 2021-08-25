## 볼링공 고르기(알고리즘 간소화)
# 2019 SW 마에스트로 입학 테스트

n, m = map(int, input().split())
ball = list(map(int, input().split()))

# 무게를 담을 리스트
array = [0] * 11
for x in ball:
    array[x] += 1

result = 0
for i in range(1, m+1):
    n -= array[i] # 무게가 i인 볼링공의 개수 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱함

print(result)