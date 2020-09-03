n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split())) # 데이터 삽입
    min_value = min(data) # 입력한 줄 중 가장 작은 수 찾기
    result = max(result, min_value) # "가장 작은 수"들 중 가장 큰 수 찾기

print(result)

